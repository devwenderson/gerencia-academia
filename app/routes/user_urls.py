from django.urls import path
from app.views.login_views import (HomePageView, CreateUserView, LoginView, DataUserView, LogoutView, 
                                   UserPasswordUpdateView, UserNameUpdateView)
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),

    # ========== AUTENTICAÇÃO ==========
    path("usuario/registrar/", CreateUserView.as_view(), name="user-create"),
    path("usuario/dados/", DataUserView.as_view(), name="user-data"),
    path("usuario/atualizar/perfil", UserNameUpdateView.as_view(), name="user-update"),
    path("usuario/atualizar/senha", UserPasswordUpdateView.as_view(), name="user-password-update"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]