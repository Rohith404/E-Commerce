from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .helpers import send_forget_password_mail


def register(request):
    if request.method == 'POST':
    	first_name = request.POST.get('first_name')
    	username = request.POST.get('username')
    	email = request.POST.get('email')
    	mobile = request.POST.get('mobile')
    	password1 = request.POST.get('password1')
    	password2 = request.POST.get('password2')
    	if password1 == password2:
    		if Profile.objects.filter(mobile = mobile).exists():
    			messages.info(request, 'Mobile number already exists!')
    			return redirect('register')
    		# check_profile = Profile.objects.filter(mobile = mobile).first()
    		# if check_profile:
    		# 	context = {'message' : 'mobile number is already registered!!!' , 'class' : 'danger' }
    		# 	return render(request,'register.html' , context)
    		if User.objects.filter(username = username).exists():
    			messages.info(request,'Username already exists')
    			return redirect('register')
    		if User.objects.filter(email = email).exists():
    			messages.info(request,'Email already exists')
    			return redirect('register')
    		else:
    			user = User.objects.create_user(first_name = first_name, username = username, email = email, password = password1)
    			user.save()
    			profile = Profile(user = user , mobile=mobile)
    			profile.save()
    			request.session['mobile'] = mobile
    			return redirect('login')
    	else:
    		messages.error(request,'password didn\'t match.')
    		return redirect('register')
    return render(request,'register.html')

def ChangePassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'change-password.html' , context)


import uuid
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget-password.html')

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
		user_obj = User.objects.filter(username = username).first()
		if user_obj is None:
			messages.success(request, 'User not found.')
			return redirect('login')
		else:
			messages.info(request,'Invalid username or password!')
			return redirect('login')
	else:
		return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')

def mobile(request):
    pros = Products.objects.all()
    return render(request, 'mobile.html', {'pros':pros})

def generatecode(self):
    pass

def laptop():
    return render(request, 'laptop.html')