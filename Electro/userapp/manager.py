from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
	use_in_migrations = True


# 	def create_user(self,first_name, username, email, mobile, password = None):

# 		if not username:
# 			raise ValueError('Username is required')

# 		username = self.normalize_username(username)
# 		user = self.model(first_name = first_name, username = username ,email = email, mobile = mobile, password = password, **extra_fields)
# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user


# 	def create_superuser(self, username, password, **extra_fields):
# 		extra_fields.setdefault('is_staff', True)
# 		extra_fields.setdefault('is_superuser', True)
# 		extra_fields.setdefault('is_active', True)

# 		if extra_fields.get ('is_staff') is not True:
# 			raise ValueError({'super user must have is_staff True'})
# 		return self.create_user(first_name, username, email, mobile, password, **extra_fields)
