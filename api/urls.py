from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'task', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
urlpatterns = (
    url(r'^', include(router.urls)),
)
