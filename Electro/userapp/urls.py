from django.urls import path
from . import views

urlpatterns = [
    # Login and Register
	path("",views.index , name = "index"),
	path("login",views.login, name = "login"),
	path("register",views.register, name = "register"),
	path("logout",views.logout, name = "logout"),
    path('forget-password/' , views.ForgetPassword , name="forget-password"),
    path('change-password/<token>/' , views.ChangePassword , name="change-password"),

    # Category
    path("mobile", views.mobile, name = "mobile"),
    path("laptop", views.laptop, name = "laptop"),
    path("cameras", views.cameras, name = "cameras"),
    path("gadgets", views.gadgets, name = "gadgets"),

    #Cart
    path("cart", views.cart, name = "cart"),
    path("<str:cate_category>/<str:prod_id>", views.productview, name = "productview"),
    path("checkout", views.checkout, name = "checkout"),
    path("add-to-cart", views.addtocart, name = "addtocart"),
    path("update-cart", views.updatecart, name = "updatecart"),
    path("delete-cart-item", views.deletecartitem, name = "deletecartitem"),

    #wishlist
    path("wishlist", views.wishlist, name = "wishlist"),
    path("add-to-wishlist", views.addtowishlist, name = "addtowishlist"),
    path("delete-wish-item", views.deletewishitem, name = "deletewishitem")
]