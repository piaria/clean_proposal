from user import UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UsersViewSet, basename='user')
urlpatterns = router.urls