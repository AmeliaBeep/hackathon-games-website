from django.shortcuts import render
from django.views import generic
from .forms import PostForm
from .models import Post


# Create your views here.


class PostList(generic.ListView):
    """View to list all posts.

    Post objects can be accessed in the template through post_list
    """

    queryset = Post.objects.all()
    template_name = "homefeed/home.html"

#@login_required
def create_post(request):
    """
    """

    # # Handle if POST request
    # if request.method == "POST":
    #     post_form = PostForm(request.POST, request.FILES)

    #     # Get the image from the request.
    #     # If unable then add an error to form to make it invalid.
    #     try:
    #         image = request.FILES.get('image')
    #         content_type = image.content_type
    #         valid_content = ["image/jpeg", "image/png", "image/svg+xml"]
    #         if content_type not in valid_content:
    #             messages.add_message(
    #                 request, messages.ERROR,
    #                 'File uploaded not one of the accepted types. '
    #                 'Please try uploading an image of JPG, PNG or SVG format.'
    #             )
    #             raise ValueError(
    #                 f'File content_type not in {valid_content}. '
    #                 + 'Instead it was {content_type}.')
    #     except (AttributeError, ValueError) as error:
    #         post_form.add_error('image', error)

    #     # Save valid post or redirect on error.
    #     if post_form.is_valid():
    #         profile_queryset = UserProfile.objects.filter(user=request.user)
    #         author_profile = get_object_or_404(profile_queryset)
    #         post = post_form.save(commit=False)
    #         post.author = author_profile
    #         post.save()
    #         messages.add_message(
    #             request, messages.SUCCESS,
    #             'Post submitted successfully!'
    #         )
    #         return HttpResponseRedirect(reverse('homefeed'))
    #     else:
    #         messages.add_message(
    #             request, messages.ERROR,
    #             'Post failed to submit!'
    #         )
    #         return HttpResponseRedirect(reverse('homefeed'))

    # Render page if GET request.
    # else:
    post_form = PostForm()
    return render(
        request,
        "homefeed/create_user_post.html",
        {
            "post_form": post_form,
        }
    )


# def edit_post(request, post_id):
#     """Handles POST and GET requests related to post editing.

#     For POST requests, the target post in the database is updated:
#         - The post has its text field set according to the form contents
#         included in the request.

#     For GET requests, render the webpage for editing a target post.

#     Args:
#         request (HttpRequest): The request to process post editing or to
#         serve the corresponding webpage
#         post_id (int): The id of the post to edit.


#     Returns:
#         Union[HttpRequest, HttpResponse]:
#             - Upon handling a POST request, a redirect request including a
#             success message.
#             - Upon handling a GET request, a response containing the page
#             and the post edit form to render.
#     """

#     post = get_object_or_404(Post, pk=post_id)

#     # Redirect unauthorised users back to home page
#     if not request.user.is_authenticated or request.user != post.author.user:
#         messages.add_message(
#             request, messages.ERROR,
#             'Not authorised to edit this post!'
#         )
#         return HttpResponseRedirect(reverse('feed'))

#     # Handle if POST request
#     if request.method == "POST":
#         post_form = PostTextForm(request.POST, instance=post)

#         # Save valid post update or redirect on error.
#         if post_form.is_valid() and post.author.user == request.user:
#             post = post_form.save(commit=True)
#             messages.add_message(request, messages.SUCCESS, 'Post updated!')
#         else:
#             messages.add_message(request, messages.ERROR,
#                                  'Error updating post!')
#         return HttpResponseRedirect(reverse('feed'))

#     # Render page if GET request.
#     else:
#         post_text_form = PostTextForm(initial={'text': post.text})
#         return render(
#             request,
#             "mainfeed/edit_post.html",
#             {
#                 "post": post,
#                 "post_text_form": post_text_form,
#             },
#         )


# def delete_post(request, post_id):
#     """Handles a request to delete a post.

#     Args:
#         request (HttpRequest): The request to process the deletion.
#         post_id (int): The id of the post to delete.

#     Returns:
#         HttpResponse: a redirect request including a success message.
#     """

#     post = get_object_or_404(Post, pk=post_id)

#     # Delete post if authorised or redirect on error.
#     if request.user.is_authenticated and request.user == post.author.user:
#         post.delete()
#         messages.add_message(request, messages.SUCCESS, 'Post deleted!')
#     else:
#         messages.add_message(request, messages.ERROR,
#                              'Not authorised to delete this post!')
#     return HttpResponseRedirect(reverse('feed'))