from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from task import views

urlpatterns = ([
    #url(r'^$', views.api_root),
    url(r'^admin/', admin.site.urls),

    url(r'^task/', include('task.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/',include('api.urls'))
])
