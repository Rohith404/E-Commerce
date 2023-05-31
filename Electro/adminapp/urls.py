from django.urls import path
from . import views

urlpatterns = [
	# Admin Login And Logout
	path("admin-login", views.admin_login, name = "admin_login"),
	path("home", views.home, name = "home"),
	path("admin-logout", views.admin_logout, name = "admin_logout"),

	# Product Table
	path("products", views.products, name = "products"),
	path("add-products", views.add_products, name = "add_products"),
	path("product-update/<str:category>/<int:id>", views.product_update, name = "product_update"),
	path("delete-product/<str:id>", views.delete_product, name = "delete_product"),

	# Users Table
	path("users", views.users, name = "users"),
	path("add-users", views.add_users, name = "add_users"),
	path("update-user/<str:id>", views.update_user, name = "update_user"),
	path("delete-user/<str:id>", views.delete_user, name = "delete_user"),

	# Orders
	path("orders", views.orders, name = "orders"),
]