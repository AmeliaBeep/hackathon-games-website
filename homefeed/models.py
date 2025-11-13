from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


# Post model
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
        )
    image = CloudinaryField('image', blank=False, default="no-post-image.jpg")
    caption = models.CharField(max_length=120, blank=False)
    text = models.CharField(max_length=999, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.user.username}'s post on {self.date_posted.strftime('%d-%m-%Y %H:%M:%S')}"

# Reaction model
class Reaction(models.Model):
    REACTION_TYPES = [
        ('like', 'Like'),
        ('laugh', 'Laugh'),
        ('sad', 'Sad'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reactions'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='reactions'
    )
    reaction_type = models.CharField(
        max_length=10, choices=REACTION_TYPES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_user_post_reaction')
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} reacted {self.reaction_type} to {self.post.id}"
    
