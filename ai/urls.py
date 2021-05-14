# coding=utf-8

from . import views
from django.conf.urls import url, include

app_name = 'ai'

urlpatterns = [
    # url(r'^cbcshelpapi/', include(router.urls), name='cbcsapi'),
    url(r'heart_predict/$', views.heart_disease, name="gpa_predict"),

    ]
