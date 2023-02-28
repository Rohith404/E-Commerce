from django.urls import path
from . import views

urlpatterns = [
	path("",views.index , name = "index"),
	path("otp", views.index, name = "otp"),
	path("login",views.login, name = "login"),
	path("register",views.register, name = "register"),
	path("logout",views.logout, name = "logout"),
	path("login_attempt",views.login_attempt , name="login"),
    path("login-otp", views.login_otp , name="login_otp"),
]