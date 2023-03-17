from django.contrib import admin
from .models import *
# # from .models import Profile
# from .models import User
# from django.contrib.auth.admin import UserAdmin

admin.site.register(Products)

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(User, UserAdmin)
admin.site.register(member)
admin.site.register(Profile)
admin.site.register(Mobile)
admin.site.register(Laptop)
admin.site.register(Camera)
admin.site.register(Gadget)