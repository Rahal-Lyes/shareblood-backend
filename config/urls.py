from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/register/", views.register),
    path("api/v1/login/", views.login),
    path("api/v1/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/calendar/", include("agenda.urls")),
    path("api/v1/shop/",include('shop.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
