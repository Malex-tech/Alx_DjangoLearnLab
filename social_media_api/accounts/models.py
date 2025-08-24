from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

# Users I follow
followers = models.ManyToManyField(
    'self',
    symmetrical=False,
    blank=True,
    related_name='user_followers'
)
following = models.ManyToManyField(
    'self',
    symmetrical=False,
    blank=True,
    related_name='user_following'
)

def __str__(self):
        return self.username
