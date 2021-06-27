from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

import imagekit
import imagekit.models
import imagekit.processors

from slugify import slugify

class Icon(imagekit.ImageSpec):
    processors = [imagekit.processors.ResizeToFill(64, 64)]
    format = 'PNG'

class CardHeader(imagekit.ImageSpec):
    processors=[
        imagekit.processors.Adjust(contrast=0.8, color=1), 
        imagekit.processors.ResizeToFill(338, 200)
    ]
    format="PNG"

class PageHeader(imagekit.ImageSpec):
    processors=[
        imagekit.processors.Adjust(contrast=0.8, color=1), 
        imagekit.processors.ResizeToFill(1024, 200)
    ]
    format="PNG"

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='member_profiles', null=True, blank=True)
    avatar = imagekit.models.ImageSpecField(source='profile_picture', spec=Icon)
    discord_username = models.CharField(max_length=64, null=True, blank=True)

    @property
    def avatar_url(self):
        if self.profile_picture:
            return self.avatar.url
        else:
            return None

    def __str__(self):
        return self.user.username

class MemberServer(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=256)
    server_url = models.URLField()
    website_url = models.URLField(blank=True, null=True)
    discord_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='server/profiles', null=True, blank=True)
    card_header = imagekit.models.ImageSpecField(source='profile_picture', spec=CardHeader)
    page_header = imagekit.models.ImageSpecField(source='profile_picture', spec=PageHeader)

    @property
    def slug(self):
        return slugify(self.name)

    @property
    def card_header_url(self):
        if self.profile_picture:
            return self.card_header.url
        else:
            return None

    @property
    def page_header_url(self):
        if self.profile_picture:
            return self.page_header.url
        else:
            return None

    def get_absolute_url(self):
        return reverse("show_server", kwargs={"server_id": self.id, "server_slug":self.slug})
    
    def __str__(self):
        return self.name