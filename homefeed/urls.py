from django.urls import path  # import path, similar to project's urls.py

from . import views  # import views.py from the current directory

urlpatterns = [
    path('', views.display_posts, name='homefeed'),
    path('create-post', views.create_post, name='create_post'),
    path('edit-post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete-post/<int:post_id>', views.delete_post, name='delete_post'),
    path(
        'posts/<int:post_id>/react/',
        views.add_reaction,
        name='add_reaction',
    ),
]
