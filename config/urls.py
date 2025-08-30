from django.urls import path, include
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
  path('api/v1/accounts/', include('accounts.urls')),
  path('api/v1/headers/', include('header_configs.urls')),
  path("api/v1/calendar/", include("agenda.urls")),
  path('api/v1/pdf/', include('pdf.urls')),
]
