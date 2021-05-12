from django.db import models

# Create your models here.


class Project(models.Model):
    """ create project name with Regression / Classification """
    PROJECT_TYPE = (('C', 'Classification'),
                    ('R', 'Regression'),
                    )
    project_name = models.CharField(max_length=150, verbose_name='Project name')
    project_type = models.CharField(max_length=1, choices=PROJECT_TYPE)

    def __str__(self):
        return "{0} - {1}".format(self.project_name, self.project_type)
