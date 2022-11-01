from user.api.views.users_viewset import UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UsersViewSet, basename='user')
urlpatterns = router.urls