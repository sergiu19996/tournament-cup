from django.db import models
from django.db.models.singals import post_save
from django.contrib.auth.models import User 


class Profile(models.Model):
    woner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=225, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        umppload_to='image/', default='../default_profile_ajrmwv'
    )

class Meta:
    ordering = ['-created_at']


def __str__(self):
    return f"{self.owner}'s profile"


def create_profile(sendeer, instance, created, **kwargs)=
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)