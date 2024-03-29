from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserViewSet, basename='user-viewset')


urlpatterns = [
    path('', include(router.urls)),
]
