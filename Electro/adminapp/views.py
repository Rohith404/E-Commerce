from userapp.models import Product, Order, OrderItem, User, Category, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib import messages

def admin_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None and user.is_superuser:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request,'Invalid username or password')
			return redirect('admin_login')
	return render(request, 'adminlogin.html')

@login_required(login_url = 'admin_login')
def home(request):
	total_count = Order.objects.count()
	users = User.objects.count()
	cate = Category.objects.count()
	prod = Product.objects.count()
	context = {'total_count' : total_count, 'users' : users, 'cate' : cate, 'prod' : prod}
	return render(request, "home.html", context)

@login_required(login_url = 'admin_login')
def products(request):
	pro = Product.objects.all()
	context = {'pro' : pro}
	return render(request, "products.html", context)

@login_required(login_url = 'admin_login')
def add_products(request):
	if request.method == 'POST':
		category_name = request.POST.get('category')
		category = Category.objects.get(category = category_name)
		product = request.POST.get('product')
		if len(request.FILES) != 0:	
			img = request.FILES['img']
		quantity = request.POST.get('quantity')
		description = request.POST.get('description')
		offer_price = request.POST.get('offer_price')
		original_price = request.POST.get('original_price')

		pro = Product(
			category = category,
			product = product,
			img = img,
			quantity = quantity,
			description = description,
			offer_price = offer_price,
			original_price = original_price,
		)
		pro.save()

		messages.success(request, "Product Added Successfully")
		return redirect('products')

	return render(request, 'home.html')

@login_required(login_url = 'admin_login')
def product_update(request, category, id):
	if request.method == 'POST':
		category_name = request.POST.get('category')
		category = Category.objects.get(category = category_name)
		product = request.POST.get('product')
		if len(request.FILES) != 0:	
			img = request.FILES['img']
		quantity = request.POST.get('quantity')
		description = request.POST.get('description')
		offer_price = request.POST.get('offer_price')
		original_price = request.POST.get('original_price')

		pro = Product(
			id = id,
			category = category,
			product = product,
			img = img,
			quantity = quantity,
			description = description,
			offer_price = offer_price,
			original_price = original_price,
		)
		pro.save()

		messages.success(request, "Product Updated Successfully")
		return redirect('products')

	return render(request, 'home.html')

@login_required(login_url = 'admin_login')
def delete_product(request, id):
	pro = Product.objects.filter(id = id)
	pro.delete()

	context = {'pro' : pro}

	messages.success(request, "Product Deleted Successfully")
	return redirect('products')


@login_required(login_url = 'admin_login')
def users(request):
	user = User.objects.all()
	profile = Profile.objects.all()
	context = {'user' : user, 'profile'  : profile}
	return render(request, 'users.html', context)

@login_required(login_url = 'adminlogin')
def add_users(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		password = request.POST.get('password')

		user = User.objects.create_user(
			first_name = first_name, 
			username = username, 
			email = email,
			password = password,
		)
		user.save()
		profile = Profile(
			user = user,
			mobile = mobile,
		)
		profile.save()

		messages.success(request, "User Added Successfully")
		return redirect('users')

	return render(request, 'home.html')

@login_required(login_url = 'admin_login')
def update_user(request, id):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		password = request.POST.get('password')

		user = User(
			id = id,
			first_name = first_name,
			username = username,
			email = email,
			password = password,
		)
		user.save()

		profile = Profile(
			id = id,
			user = user,
			mobile = mobile,
		)
		profile.save()
		messages.success(request, "User Updated Successfully")
		return redirect('users')

	return redirect(request, 'users.html')

@login_required(login_url = 'admin_login')
def delete_user(request, id):
	user = User.objects.filter(id = id)
	user.delete()

	context = {'user' : user}

	messages.success(request, "User Deleted Successfully")
	return redirect('users')


@login_required(login_url = 'admin_login')
def orders(request):
	order = OrderItem.objects.all()
	context = {'order' : order}
	return render(request, 'orders.html', context)

def admin_logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'Logout successfully')
		return redirect('admin_login')
	return redirect('home')