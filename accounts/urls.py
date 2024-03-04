from django.urls import path
from . import views

app_name="accounts"
urlpatterns=[
    path("",views.LoginAppView.as_view(),name="login"),#  Appele de la vue baser sur la classe
    path("logout",views.LogoutUserView.as_view(),name="logout"),
    path("register",views.register_app,name="register"),
    path("Mot de passe oublier", views.pass_forgeted,name="pass_forgeted")
]