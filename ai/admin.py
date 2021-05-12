from django.contrib import admin

# Register your models here.
from .models import Project
from .own import create_ml_project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_type']

    def save_form(self, request, form, change):
        p = create_ml_project.create_project(request.POST.get('project_name'))
        return super(ProjectAdmin, self).save_form(request, form, change)


