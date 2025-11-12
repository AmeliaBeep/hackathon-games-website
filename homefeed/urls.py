from django.urls import path  # import path, similar to project's urls.py

from . import views  # import views.py from the current directory

urlpatterns = [
    path('', views.PostList.as_view(), name='homefeed'),
    path('create-post', views.create_post, name='create_post'),
    path('edit-post/<int:post_id>', views.edit_post, name='edit_post'),
]
