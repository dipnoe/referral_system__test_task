from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', ..., basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
