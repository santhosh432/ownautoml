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
    data = models.FileField(null=True, blank=True, upload_to=user_directory_path)

    def __str__(self):
        return "{0} - {1}".format(self.project_name, self.project_type)
