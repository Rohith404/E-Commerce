from django.db import models
from django.contrib.auth.models import User
# import uuid

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14)
    forget_password_token = models.CharField(max_length=100)

    def __str__(self):
        return self.mobile

class Category(models.Model):
	category = models.CharField(max_length = 100, blank = False, null = False)

	def __str__(self):
		return self.category

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	img = models.ImageField(upload_to = 'pics')
	product = models.CharField(max_length = 150, default = '')
	quantity = models.IntegerField(null = False, blank = False, default = '1')
	description = models.CharField(max_length = 250, default = '')
	original_price = models.IntegerField()
	offer_price = models.IntegerField()

	def __str__(self):
		return self.product

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.IntegerField(null = False, blank = False)
	created_at = models.DateTimeField(auto_now_add = True)

class Liked(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)



class member(models.Model):
	name = models.CharField(max_length = 100)

