from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    avatar_url = models.URLField(
        default="https://cdn-icons-png.flaticon.com/512/686/686589.png"
    )

    is_adult = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.username