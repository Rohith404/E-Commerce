from django.db import models

class Products(models.Model):
	img = models.ImageField(upload_to = 'pics')
	category = models.CharField(max_length = 100)
	product_name = models.CharField(max_length = 100)
	price = models.IntegerField()
	price1 = models.IntegerField()

	def __str__(self):
		return self.product_name
