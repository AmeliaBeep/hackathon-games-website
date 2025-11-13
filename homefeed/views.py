from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import generic

from .forms import PostForm
from .models import Post, Reaction
from django.db.models import Count, Q

# Create your views here.


class PostList(generic.ListView):
    """View to list all posts.

    Post objects can be accessed in the template through post_list
    """
    template_name = "homefeed/home.html"

    queryset = (
        Post.objects
        .annotate(
            like_count=Count('reactions', filter=Q(reactions__reaction_type='like')),
            laugh_count=Count('reactions', filter=Q(reactions__reaction_type='laugh')),
            sad_count=Count('reactions', filter=Q(reactions__reaction_type='sad')),
        )
        .order_by('-date_posted')
    )

@login_required
def create_post(request):

    # Handle if POST request.
    if request.method == "POST":
        handle_post_update(request, operation="Create")
        return HttpResponseRedirect(reverse('homefeed'))

    # Render page if GET request.
    else:
        post_form = PostForm()
        return render(
            request,
            "homefeed/create_user_post.html",
            {
                "post_form": post_form,
            }
        )

@login_required
def edit_post(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    # Redirect unauthorised users back to home page.
    if request.user != post.user:
        messages.add_message(
            request, messages.ERROR,
            'Not authorised to edit this post!'
        )
        return HttpResponseRedirect(reverse('homefeed'))

    # Handle if POST request.
    if request.method == "POST":
        handle_post_update(request, operation="Update", instance=post)
        return HttpResponseRedirect(reverse('homefeed'))


    # Render page if GET request.
    else:
        post_form = PostForm(
            initial={'caption':post.caption,
                     'text': post.text,
                     'image':post.image, })

        return render(
            request,
            "homefeed/edit_user_post.html",
            {
                "post": post,
                "post_form": post_form,
            },
        )

def delete_post(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    # Delete post if authorised or redirect on error.
    if request.user.is_authenticated and  request.user == post.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'Not authorised to delete this post!')
    return HttpResponseRedirect(reverse('homefeed'))


def handle_post_update(request, operation, instance=None):
    """Handles the POST request to update a post, or create a new one.

    The PostForm object is constructed, including passing it any existing
    post to update if it was called by the update function.

    Images are checked to ensure they exist and to validate their content_type
    is one of the accepted values. If not, then an error is added to the
    post_form instance to make it fail its is_valid() method.

    Args:
        request (HttpRequest): The request to process the deletion.
        operation (str): The id of the post to delete.
        instance (Post): The id of the post to delete.

    Returns:
        None
    """

    post_form = PostForm(request.POST, request.FILES, instance=instance)

    # Get any image submitted
    # Make create posts fail if there is no image
    try:
        image = request.FILES.get('image')

        content_type = image.content_type
        valid_content = ["image/jpeg", "image/png", "image/svg+xml"]

        if content_type not in valid_content:
            messages.add_message(
                request, messages.ERROR,
                'File uploaded not one of the accepted types. '
                + 'Please try uploading an image of JPG, PNG or SVG format.'
            )
            raise ValueError(
                f'File content_type not in {valid_content}. '
                + f'Instead it was {content_type}.')
        
    # Raised if no image in FILES
    # Update operation should continue and ignore this error
    except AttributeError:
        if operation == 'Create':
            messages.add_message(
                request, messages.ERROR, 'Posts require an image!')
            raise AttributeError(
                f'New posts require an image.')
        else:
            pass        
    except (AttributeError, ValueError) as error:
        post_form.add_error('image', error)

    # Save valid post or add error to messages.
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.user = request.user
        post.save()
        messages.add_message(
            request, messages.SUCCESS,
            f'Post {operation} submitted successfully!'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            f'Post {operation} failed to submit!'
        )

# Reactions
@login_required
def add_reaction(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    reaction_type = request.POST.get('reaction_type','like')

    # Check for pre-exsiting reactipn
    existing_reaction = Reaction.objects.filter(user=request.user, post=post).first()
    if existing_reaction:
        if existing_reaction.reaction_type == reaction_type:
            existing_reaction.delete()
        else:
            existing_reaction.reaction_type = reaction_type
            existing_reaction.save()
    else:
        Reaction.objects.create(user=request.user, post=post, reaction_type=reaction_type)

    return redirect(request.META.get('HTTP_REFERER', '/'))
