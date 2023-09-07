from . import views
from django.urls import path

app_name="Todo"
urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login,name="login")
]
