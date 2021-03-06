from django.contrib import admin
from django.utils.safestring import mark_safe

from membersites.models import *

# Register your models here.
class MemberServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'header', 'status')
    list_filter = ('status',)
    actions = ('approve', 'reject')

    def header(self, server):
        if server.profile_picture:
            return mark_safe(
                '<img src="%s" height="64px" />' % (server.card_header_url,)
            )
        else:
            return 'None'
    header.short_description = "Header"

    def approve(self, request, queryset):
        queryset.update(status=ApprovalStatus.APPROVED)
    approve.short_description = 'Approve Servers'
        
    def reject(self, request, queryset):
        queryset.update(status=ApprovalStatus.REJECTED)
    reject.short_description = 'Reject Servers'
        
admin.site.register(MemberServer, MemberServerAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    def avatar(self, member):
        if member.profile_picture:
            return mark_safe(
                '<img src="%s" height="64px" />' % (member.avatar_url,)
            )
        else:
            return 'None'
    avatar.short_description = "Avatar"

admin.site.register(Member, MemberAdmin)

