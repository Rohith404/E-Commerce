from django.urls import path
from . import views

urlpatterns = [
	path("",views.index , name = "index"),
	path("login",views.login, name = "login"),
	path("register",views.register, name = "register"),
	path("logout",views.logout, name = "logout"),
    path('forget-password/' , views.ForgetPassword , name="forget-password"),
    path('change-password/<token>/' , views.ChangePassword , name="change-password"),
]