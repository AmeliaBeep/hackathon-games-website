from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.


class PostList(generic.ListView):
    """View to list all posts.

    Post objects can be accessed in the template through post_list
    """

    queryset = Post.objects.all()
    template_name = "homefeed/home.html"
    paginate_by = 10