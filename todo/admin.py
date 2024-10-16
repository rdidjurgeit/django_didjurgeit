from django.contrib import admin

from .models import Task, PremiumMembership

admin.site.register(Task)
admin.site.register(PremiumMembership)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
