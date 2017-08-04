from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add/$', views.add),
    url(r'^api/$', views.TaskList.as_view()),
    url(r'^api/(?P<id>\w{0,50})/$', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
