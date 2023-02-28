from django.contrib import admin
from .models import Products
from .models import Profile
# from .models import User
# from django.contrib.auth.admin import UserAdmin

admin.site.register(Products)
admin.site.register(Profile)

# admin.site.register(User, UserAdmin)
# admin.site.register(member)

