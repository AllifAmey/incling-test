from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("tile", views.TileViewset, basename='tile-viewset')
router.register("task", views.TaskViewset, basename='task-viewset')
router.register("user", views.UserViewSet, basename='user-viewset')


urlpatterns = [
    path('', include(router.urls)),
]
