from django.urls import path
from .views import login_view, home_view

urlpatterns = [
    path("home/", home_view, name="login"),
    path("login/", login_view, name="login"),
]
