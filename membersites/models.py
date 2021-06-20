from django.db import models
from django.shortcuts import reverse
from slugify import slugify

# Create your models here.
class MemberSite(models.Model):
    name = models.CharField(max_length=256)
    server = models.URLField()
    website = models.URLField(blank=True, null=True)
    discord = models.URLField(blank=True, null=True)
    description = models.TextField()

    @property
    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        #return "/sites/%s/%s/" % (self.id, self.slug)
        return reverse("show_site", kwargs={"site_id": self.id, "site_slug":self.slug})
    
    def __str__(self):
        return self.name