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
    path("deleteTodo/<int:id>",views.deletetodo,name="deleteTodo"),
    path("editTodo/<int:id>",views.editTodo,name="editTodo"),
    path('completed/<int:id>/', views.completed, name='completed'),

]
