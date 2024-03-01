from django.urls import path
from . import views

app_name="app"
urlpatterns=[
    path("Ghoster",views.index,name="index")
]