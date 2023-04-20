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

class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 100, null = False)
	latst_name = models.CharField(max_length = 100, null = False)
	email = models.CharField(max_length = 100, null = False)
	address = models.TextField(null = False)
	city = models.CharField(max_length = 100, null = False)
	country = models.CharField(max_length = 100, null = False)
	pincode = models.CharField(max_length = 100, null = False)
	phone = models.CharField(max_length = 100, null = False)
	total_price = models.FloatField(null = False)
	payment_mode = models.CharField(max_length = 100, null = False)
	payment_id = models.CharField(max_length = 250, null = True)
	order_status = (
		('Packed', 'Packed'),
		('Shiped', 'Shiped'),
		('Pending', 'Pending'),
		('Delivered', 'Delivered'),
	)
	status = models.CharField(max_length = 150, choices = order_status, default = 'Pending')
	message = models.TextField(null = True)
	tracking_no = models.CharField(max_length = 250, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return '{} - {}'.format(self.user, self.tracking_no)


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

