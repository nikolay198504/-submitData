from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PassViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'passes', PassViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
