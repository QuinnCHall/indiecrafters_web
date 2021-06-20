from django.contrib import admin

from membersites.models import *

# Register your models here.
class MemberSiteAdmin(admin.ModelAdmin):
    pass
admin.site.register(MemberSite, MemberSiteAdmin)