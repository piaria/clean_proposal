from django.urls import path

from message.api.viewset import MessagesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', MessagesViewSet, basename='message')
urlpatterns = router.urls