from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products
# from django.contrib.auth import get_user_model

# User = get_user_model()

def index(request):

	pros = Products.objects.all()

	return render(request, 'index.html', {'pros':pros})

def register(request):

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if password1 == password2:
			if User.objects.filter(username = username).exists():
				messages.info(request,'Username already exists')
				return redirect('register')
			elif User.objects.filter(email = email).exists():
				messages.info(request,'Email already exists')
				return redirect('register')
			elif User.objects.filter(mobile = mobile).exists():
				messages.info(request,'Phone Number already exists')
				return redirect('register')
			else:
				user = User.objects.create_user(first_name = first_name, username = username, email = email, mobile = mobile, password = password1)
				user.save();
				print('User registered.')
				return redirect('login')
		else:
			messages.info(request,'password didn\'t match.')
			return redirect('register')
		return redirect('/')

	else:
		return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request,'Invalid username or password!')
			return redirect('login')

	else:
		return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')
