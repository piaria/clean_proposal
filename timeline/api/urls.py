from django.urls import path

from .viewset import TimelineViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TimelineViewSet, basename='timeline')
urlpatterns = router.urls