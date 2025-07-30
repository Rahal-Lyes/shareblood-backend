from django.urls import path

from . import views


urlpatterns = [
    path('accounts/<int:id>/', views.RegisterView.as_view(), name='account-detail'),
    # 👉 Bonus : pour récupérer tous les utilisateurs ou en créer un
    path('accounts/', views.UserListCreateView.as_view(), name='account-list'),
]