from django.contrib import admin
from projectapp.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
