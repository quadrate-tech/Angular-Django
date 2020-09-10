from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('qts_api/', include(router.urls))
]
