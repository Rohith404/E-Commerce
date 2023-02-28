from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products
from .models import Profile
import random
import http.client
from django.conf import settings


def send_otp(mobile , otp):
    print("FUNCTION CALLED")
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.AUTH_KEY 
    headers = { 'content-type': "application/json" }
    url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"Your otp is "+otp +"&mobile="+mobile+"&authkey="+authkey+"&country=91"
    conn.request("GET", url , headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    return None



def login_attempt(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        
        user = Profile.objects.filter(mobile = mobile).first()
        
        if user is None:
            context = {'message' : 'User not found' , 'class' : 'danger' }
            return render(request,'login.html' , context)
        
        otp = str(random.randint(1000 , 9999))
        user.otp = otp
        user.save()
        send_otp(mobile , otp)
        request.session['mobile'] = mobile
        return redirect('login_otp')        
    return render(request,'login.html')


def login_otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            user = User.objects.get(id = profile.user.id)
            login(request , user)
            return redirect('cart')
        else:
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'login_otp.html' , context)
    
    return render(request,'login_otp.html' , context)
    
    

def register(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
        
		check_user = User.objects.filter(username = username).first()
		check_profile = Profile.objects.filter(mobile = mobile).first()
        
		if check_user or check_profile:
			context = {'message' : 'User already exists' , 'class' : 'danger' }
			return render(request,'register.html' , context)
            
		user = User(first_name = first_name, username = username, email = email, password = password1 )
		user.save()
		otp = str(random.randint(1000 , 9999))
		profile = Profile(user = user , mobile=mobile , otp = otp) 
		profile.save()
		send_otp(mobile, otp)
		request.session['mobile'] = mobile
		return redirect('otp')
	return render(request,'register.html')

def otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            return redirect('cart')
        else:
            print('Wrong')
            
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'otp.html' , context)
            
        
    return render(request,'otp.html' , context)

# User = get_user_model()

def index(request):

	pros = Products.objects.all()

	return render(request, 'index.html', {'pros':pros})

# def register(request):

# 	if request.method == 'POST':
# 		first_name = request.POST.get('first_name')
# 		username = request.POST.get('username')
# 		email = request.POST.get('email')
# 		mobile = request.POST.get('mobile')
# 		password1 = request.POST.get('password1')
# 		password2 = request.POST.get('password2')

# 		if password1 == password2:
# 			check_user = User.objects.filter(username = username).first()
# 			check_profile = Profile.objects.filter(mobile = mobile).first()

# 			if check_user or check_profile:
# 				context={'message':'User already exists','class':'danger'}
# 				return render(request,'register.html' , context)
# 			else:
# 				user = User.objects.create_user(first_name = first_name, username = username, email = email, password = password1)
# 				user.save();
# 				print('User registered.')
# 				return redirect('login')
# 		else:
# 			messages.info(request,'password didn\'t match.')
# 			return redirect('register')
# 		return redirect('/')

# 	else:
# 		return render(request, 'register.html')

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

def otp(request):
	if request.method == 'POST':
		mobile = request.POST.get('mobile')

	return render(request, 'otp.html')