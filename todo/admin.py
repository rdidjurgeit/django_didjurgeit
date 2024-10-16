from django.contrib import admin

from .models import Task, PremiumMembership

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'user', 'status', 'title']

class PremiumMembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'user', 'is_active']

admin.site.register(Task, TaskAdmin)
admin.site.register(PremiumMembership, PremiumMembershipAdmin)