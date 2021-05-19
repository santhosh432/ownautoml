from django.db import models
import os
# Create your models here.


def user_directory_path(instance, filename='train_data.csv'):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    p = os.getcwd()
    # path = 'ai/own/input/' + str(instance.project_name) + '/' + filename
    path = 'ai/own/input/' + str(instance.project_name) + '/' + 'train_data.csv'
    # print(path)
    return path


class Project(models.Model):
    """ create project name with Regression / Classification """
    PROJECT_TYPE = (('C', 'Classification'),
                    ('R', 'Regression'),
                    )
    project_name = models.CharField(max_length=150, verbose_name='Project name')
    project_type = models.CharField(max_length=1, choices=PROJECT_TYPE)
    label = models.CharField(max_length=20, default='label', verbose_name='label column name')
    data = models.FileField(null=True, blank=True, upload_to=user_directory_path)

    def __str__(self):
        return "{0} - {1}".format(self.project_name, self.project_type)


class ClassificationReport(models.Model):
    """ only classification model report """
    project_name = models.ForeignKey(Project, related_name='project_classification', on_delete=models.PROTECT)
    model_name = models.CharField(max_length=100, verbose_name='Model name')
    model_path = models.CharField(max_length=100, default='')
    activate = models.BooleanField(default=False)
    accuracy = models.FloatField()
    f1_score = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.project_name, self.model_name, self.accuracy)


