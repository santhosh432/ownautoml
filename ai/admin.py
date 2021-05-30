from django.contrib import admin

# Register your models here.
from .models import Project, ClassificationReport
from .own import create_ml_project
import os
import sys
from django.contrib import messages
from ai.own.default import create_folds, train, model_dispatcher


@admin.action(description='Create fold for the projects ....')
def make_folding(modeladmin, request, queryset):

    for q in queryset:
        print(q.project_name)
        # path = os.getcwd() + '/ai/own/src/{0}/'.format(q.project_name)
        # os.chdir(path)
        # g = os.getcwd()
        # sys.path.append(path)
        # print(os.listdir(g))

        print(sys.path)

        data_path = os.getcwd() + '/ai/own/input/{0}/train_data.csv'.format(q.project_name)
        train_path = os.getcwd() + '/ai/own/input/{0}/train_fold.csv'.format(q.project_name)
        create_folds.create_fold(data_path, train_path)
        messages.success(request, 'Fold has been created for project {0} successfully ....'.format(q.project_name))
        # sys.path.remove(path)
        # print(path)


@admin.action(description='Start training for the project ....')
def start_train(modeladmin, request, queryset):
    for q in queryset:
        path = os.getcwd() + '/ai/own/src/{0}'.format(q.project_name)
        # os.chdir(path)
        print('He cwd after :-----------',os.getcwd())
        # g = os.chdir(path)
        # g = os.getcwd()
        # sys.path.append(path)
        print(path)
        # import train
        # import model_dispatcher
        import inspect
        # print('File path -----------------------------------',inspect.getmodule(train.__class__))
        models = model_dispatcher.models

        for model in models:
            train_path = os.getcwd() + '/ai/own/input/{0}/train_fold.csv'.format(q.project_name)

            for i in range(5):
                report = train.run(i,
                                   model,
                                   project_name=q.project_name,
                                   file_path=train_path)
                # print(report)
                save_report = ClassificationReport(project_name=q,
                                                   model_name=report.get('model_name'),
                                                   model_path = report.get('model_file', None),
                                                   accuracy=report.get('accuracy', 0),
                                                   f1_score=report.get('f1', 0),
                                                   precision=report.get('precision', 0),
                                                   recall=report.get('recall', 0),
                                                   )
                save_report.save()
                # os.chdir(os.getcwd())

                # messages.info(request, 'Train with fold number {0} completed by model {1} ....'.format(i, model))
        # sys.path.remove(path)

    messages.success(request, 'Training successfully completed ... ')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_type']
    actions = [make_folding, start_train]

    def save_form(self, request, form, change):
        p = create_ml_project.create_project(request.POST.get('project_name'))
        return super(ProjectAdmin, self).save_form(request, form, change)


@admin.register(ClassificationReport)
class ClassificationReportAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'model_name','activate','accuracy', 'date_created']
    list_filter = ['model_name', 'project_name']
    list_editable = ['activate']

