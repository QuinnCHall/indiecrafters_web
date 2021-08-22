from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.staticfiles import finders as staticfiles_finders
from django.core.files import File
from django import forms

import os
import random
import imagekit
import imagekit.models
import imagekit.processors

from slugify import slugify

DEFAULT_SERVER_IMAGES = [
    'img/default/server/ice.png',
    'img/default/server/underwater.png',
    'img/default/server/endgame.png',
    'img/default/server/rockarch.png',
    'img/default/server/beach.png',
    'img/default/server/village.png',
    'img/default/server/desert.png',
    'img/default/server/mountains.png',
    'img/default/server/nether.png',
]
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

class ApprovalStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'

class MemberServer(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=256, verbose_name='Server Name')
    status = models.CharField(max_length=16, choices=ApprovalStatus.choices, default=ApprovalStatus.PENDING)
    server_url = models.CharField(max_length=256, blank=True, null=True)
    website_url = models.CharField(max_length=256, blank=True, null=True)
    discord_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    #default_picture = models.CharField(max_length=256, blank=True, null=True)
    profile_picture = models.ImageField(verbose_name='Server Screenshot', upload_to='server/profiles', null=True, blank=True)
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.profile_picture:
            filepath = staticfiles_finders.find(random.choice(DEFAULT_SERVER_IMAGES))
            file = File(open(filepath, "rb"))
            file_name = os.path.basename(file.name)
            self.profile_picture.save(file_name, file, save=True)

class MemberServerForm(forms.ModelForm):
    class Meta:
        model = MemberServer
        exclude = ['owner', 'status']
