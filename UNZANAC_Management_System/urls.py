from django.contrib import admin
from django.urls import path, include
from .views import home  # <-- Add this import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', home, name='home'),  # <-- Add this line
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('auth_app.urls')),
    path('commitees/', include('commitees.urls')),
    path('donations/', include('donations.urls')),
    path('events/', include('events.urls')),
    path('finance/', include('finance.urls')),
    path('members/', include('members.urls')),
    path('notifications/', include('notifications.urls')),
]
