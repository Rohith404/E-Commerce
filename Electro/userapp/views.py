from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products

def index(request):

	pros = Products.objects.all()

	return render(request, 'index.html', {'pros':pros})

def register(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username already exists')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email already exists')
				return redirect('register')
			else:
				user = User.objects.create_user(first_name = first_name, username = username, email = email, password = password1)
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
		username = request.POST['username']
		password = request.POST['password']

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
