from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    # Все роуты API должны быть в v1/
    path('v1/', include(router.urls)),
    # Тестам нужен именно этот эндпоинт для получения токена
    path('v1/api-token-auth/', views.obtain_auth_token),
]
