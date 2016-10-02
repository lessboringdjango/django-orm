from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/grade/(?P<which>\d+)/$', views.grade_api, name='grade_api'),
]
