from django.conf.urls import url

from task import views

urlpatterns = [
    url(r'^$', views.TaskList.as_view(), name='task-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='task-detail'),
]
