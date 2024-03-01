from django.urls import path
from . import views

app_name="account"
urlpatterns=[
    path("",views.login_app,name="login"),
    path("logout",views.logout_app,name="logout"),
    path("register",views.register_app,name="register"),
    path("Mot de passe oublier", views.pass_forgeted,name="pass_forgeted")
]