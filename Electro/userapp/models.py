from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class UserCustomManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, first_name, username, email, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('The given phonenumber must be set')
        user = self.model(first_name = first_name, username = username, email = email, phone_number=phone_number, username = password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,first_name, username, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, first_name, username, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(first_name, username, email, phone_number, password, **extra_fields)


class User(AbstractUser):
    # You have to remove 'username' and 'password'!
    # username = None
    # password = None
    email = models.EmailField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.IntegerField(unique=True)
    is_owner = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    name = models.CharField(max_length=40)
    image = models.ImageField(blank=True, null=True)
    data_join = models.DateTimeField(default=timezone.now)
    code_agency = models.IntegerField(null=True, blank=True, default=0)

    USERNAME_FIELD = 'phone_number'
    # You must remove the 'phone_number' from REQUIRED_FIELDS!
    # Here you can't repeat in the REQUIRED_FIELDS the same field that you put in USERNAME_FIELD, you can add other: 'email', etc ...
    REQUIRED_FIELDS = []
    

    objects = UserCustomManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

































# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # from .manager import UserManager
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser

# class CustomUser(AbstractBaseUser):
# 	user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user')
# 	first_name = models.CharField(max_length = 100,blank = True)
# 	username = models.CharField(max_length = 50, unique = True, default = '')
# 	email = models.EmailField(max_length = 50, unique = True, default = '')
# 	mobile = models.CharField(max_length = 14)
# 	password = models.CharField(max_length = 100, default = '')


# 	REQUIRED_FIELDS = []
# 	USERNAME_FIELD = 'username'

# # class User(AbstractUser):
# # 	mobile = models.CharField(max_length = 14)

# # class User(AbstractUser):
# # 	first_name = models.CharField(max_length = 100,blank = True)
# # 	username = models.CharField(max_length = 50, unique = True, default = '')
# # 	email = models.EmailField(max_length = 50, unique = True, default = '')
# # 	mobile = models.CharField(max_length = 14)
# # 	password = models.CharField(max_length = 100, default = '')
# # 	is_verified = models.BooleanField(default = False)
# # 	email_token = models.CharField(max_length = 100, null = True, blank = True)
# # 	forget_password = models.CharField(max_length = 100, null = True, blank = True)
# # 	last_login_time = models.DateTimeField(null = True, blank = True)
# # 	last_logout_time = models.DateTimeField(null = True, blank = True)

# # 	objects = UserManager()

# # 	


# class Products(models.Model):
# 	img = models.ImageField(upload_to = 'pics')
# 	category = models.CharField(max_length = 100)
# 	product_name = models.CharField(max_length = 100)
# 	price = models.IntegerField()
# 	price1 = models.IntegerField()

# 	def __str__(self):
# 		return self.product_name

# # # class Profile(models.Model):
# # # 	user = models.OneToOneField(User, on_delete = models.CASCADE)
# # # 	mobile = models.CharField(max_length = 13)
# # # 	otp = models.CharField(max_length = 6)


# # class User(models.Model):
# # 	user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user')
# # 	phone_number = models.CharField(max_length = 13)

# # # class UserRegModel(models.Model):
# # #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# # #     mobile = models.CharField(max_length=100)

# # class member(models.Model):
# # 	first_name = models.CharField(max_length = 100)
# # 	username = models.CharField(max_length = 100)
# # 	email = models.EmailField(max_length = 100)
# # 	mobile = PhoneField(null=False, blank=False, unique=True)
# # 	password = models.CharField(max_length = 15, default = '')

# # 	def __str__(self):
# # 		return self.username