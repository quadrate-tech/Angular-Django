from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/token', TokenObtainPairView.as_view(), name="auth_token"),
    path('api/auth/refresh',TokenRefreshView.as_view,name="auth_refresh_token")
]
