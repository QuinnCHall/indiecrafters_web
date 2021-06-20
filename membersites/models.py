from django.db import models

# Create your models here.
class MemberSite(models.Model):
    name = models.CharField(max_length=256)
    server = models.URLField()
    website = models.URLField(blank=True, null=True)
    discord = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name