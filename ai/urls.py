# coding=utf-8

from . import views
from django.conf.urls import url, include

app_name = 'ai'

urlpatterns = [
    # url(r'^cbcshelpapi/', include(router.urls), name='cbcsapi'),
    url(r'predict/(?P<pk>\d+)/', views.heart_disease, name="predict"),

    ]
