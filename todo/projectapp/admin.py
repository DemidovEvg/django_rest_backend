from django.contrib import admin
from projectapp.models import Todo, Project


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
