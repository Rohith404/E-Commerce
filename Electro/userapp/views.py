from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

def register(request):
    if request.method == 'POST':
    	first_name = request.POST.get('first_name')
    	username = request.POST.get('username')
    	email = request.POST.get('email')
    	mobile = request.POST.get('mobile')
    	password = request.POST.get('password')
    	check_user = User.objects.filter(username = username).first()
    	check_user = User.objects.filter(email = email).first()
    	check_profile = Profile.objects.filter(mobile = mobile).first()
    	if check_user or check_profile:
    		context = {'message' : 'Username or email already taken' , 'class' : 'danger' }
    		return render(request,'register.html' , context)
    	user = User(first_name = first_name, username = username, email = email, password = password)
    	user.save()
    	profile = Profile(user = user , mobile=mobile)
    	profile.save()
    	request.session['mobile'] = mobile
    	return redirect('login')
    return render(request,'register.html')

def index(request):

	pros = Products.objects.all()

	return render(request, 'index.html', {'pros':pros})


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