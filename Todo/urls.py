from . import views
from django.urls import path

app_name="Todo"
urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("register/",views.register,name="register"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addtodo/",views.addtodo,name="addtodo"),
]
