# Generated by Django 3.2.2 on 2021-05-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0005_alter_classificationreport_model_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationreport',
            name='activate',
            field=models.BooleanField(default=False),
        ),
    ]
