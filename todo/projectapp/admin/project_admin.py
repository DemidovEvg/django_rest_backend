from django.contrib import admin
from projectapp.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
