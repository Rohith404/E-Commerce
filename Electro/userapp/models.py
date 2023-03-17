from django.db import models
from django.contrib.auth.models import User

class Mobile(models.Model):
	img = models.ImageField(upload_to = 'pics')
	brand = models.CharField(max_length = 100)
	model_name = models.CharField(max_length = 100)
	price = models.IntegerField()

	def __str__(self):
		return self.model_name

class Laptop(models.Model):
	img = models.ImageField(upload_to = 'pics')
	brand = models.CharField(max_length = 100)
	model_name = models.CharField(max_length = 100)
	price = models.IntegerField()

	def __str__(self):
		return self.model_name

class Camera(models.Model):
	img = models.ImageField(upload_to = 'pics')
	brand = models.CharField(max_length = 100)
	model_name = models.CharField(max_length = 100)
	price = models.IntegerField()

	def __str__(self):
		return self.model_name

class Gadget(models.Model):
	img = models.ImageField(upload_to = 'pics')
	category = models.CharField(max_length = 100)
	model_name = models.CharField(max_length = 100)
	price = models.IntegerField()

	def __str__(self):
		return self.model_name

class Products(models.Model):
	img = models.ImageField(upload_to = 'pics')
	category = models.CharField(max_length = 100)
	product_name = models.CharField(max_length = 100)
	price = models.IntegerField()
	price1 = models.IntegerField()

	def __str__(self):
		return self.product_name

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14)
    forget_password_token = models.CharField(max_length=100)

    def __str__(self):
        return self.mobile

class member(models.Model):
	first_name = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	mobile = models.CharField(null=False, blank=False, unique=True, max_length = 14)
	password = models.CharField(max_length = 100, default = '')

	def __str__(self):
		return self.username