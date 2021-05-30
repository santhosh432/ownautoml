# coding=utf-8

from . import views
from django.conf.urls import url, include
from rest_framework import routers
from .api import ProjectViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)

# urlpatterns = router.urls


app_name = 'ai'

urlpatterns = [
    url('', include(router.urls)),
    url(r'predict/(?P<pk>\d+)/', views.main_predict, name="predict"),


    ]
