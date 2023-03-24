from django.db import models
from django.contrib.auth.models import User

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
	product_name = models.CharField(max_length = 100)
	quantity = models.IntegerField(null = False, blank = False, default = '1')
	original_price = models.IntegerField()
	offer_price = models.IntegerField()

	def __str__(self):
		return self.product_name

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.IntegerField(null = False, blank = False)
	created_at = models.DateTimeField(auto_now_add = True)


class member(models.Model):
	name = models.CharField(max_length = 100)

