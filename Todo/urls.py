from . import views
from django.urls import path

app_name="Todo"
urlpatterns = [
    path("",views.index,name="index"),
]
