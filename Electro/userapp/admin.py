from django.contrib import admin
from .models import Products
from django.contrib.auth.admin import UserAdmin
# from .models import member
from .models import User

admin.site.register(Products)
admin.site.register(User, UserAdmin)
# admin.site.register(member)

