from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet, UserCreate
from rest_framework.authtoken import views as drf_views

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='register'),
    path('api-token-auth/', drf_views.obtain_auth_token, name='api-token-auth'),
]