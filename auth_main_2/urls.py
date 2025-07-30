from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

urlpatterns = [

    path("api/v1/register/", views.register),
    path("api/v1/login/",views.login),
    path("api/v1/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/v1/',include('accounts.urls'))
    
]
