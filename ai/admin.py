from django.contrib import admin

# Register your models here.
from .models import Project
from .own import create_ml_project
import os
import sys
from django.contrib import messages


@admin.action(description='Create fold for the projects ....')
def make_folding(modeladmin, request, queryset):

    for q in queryset:
        path = os.getcwd() + '/ai/own/src/{0}/'.format(q.project_name)
        os.chdir(path)
        g = os.getcwd()
        sys.path.append(path)
        # print(os.listdir(g))

        import create_folds

        create_folds.create_fold()
        messages.success(request, 'Fold has been created for project {0} successfully ....'.format(q.project_name))
        # print(path)


@admin.action(description='Start training for the project ....')
def start_train(modeladmin, request, queryset):
    for q in queryset:
        path = os.getcwd() + '/ai/own/src/{0}/'.format(q.project_name)
        # g = os.chdir(path)
        # g = os.getcwd()
        sys.path.append(path)
        print(path)
        import train
        import model_dispatcher

        models = model_dispatcher.models

        for model in models:

            for i in range(5):
                train.run(i, model)
                messages.info(request, 'Train with fold number {0} completed by model {1} ....'.format(i, model))

    messages.success(request, 'Training complete successfully ')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_type']
    actions = [make_folding, start_train]

    def save_form(self, request, form, change):
        p = create_ml_project.create_project(request.POST.get('project_name'))
        return super(ProjectAdmin, self).save_form(request, form, change)

