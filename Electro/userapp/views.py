from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .helpers import send_forget_password_mail
from django.contrib.auth.decorators import login_required

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
    			messages.error(request, 'Mobile number already exists!')
    			return redirect('register')
    		if User.objects.filter(username = username).exists():
    			messages.error(request,'Username already exists')
    			return redirect('register')
    		if User.objects.filter(email = email).exists():
    			messages.error(request,'Email already exists')
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
                messages.error(request, 'No user found with this username.')
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
    pros = Product.objects.all()
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
			messages.error(request, 'User not found.')
			return redirect('login')
		else:
			messages.error(request,'Invalid username or password!')
			return redirect('login')
	else:
		return render(request,'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('/')

def productview(request, cate_category, prod_id):
    if(Category.objects.filter(category = cate_category)):
        if(Product.objects.filter(id = prod_id)):
            prod = Product.objects.filter(id = prod_id).first
            pros = Product.objects.all()
            products = Product.objects.all()
            context = {'prod':prod, 'products':products, 'pros':pros}
        else:
            messages.error(request, "No such product found!")
            return redirect('/')
    else:
        messages.error(request, "No such category found!")
        return redirect('/')
    return render(request, 'productview.html', context)

def mobile(request):
    mobiles = Category.objects.get(category = 'Mobile')
    mobs = Product.objects.filter(category = mobiles)
    return render(request, 'mobile.html', {'mobs':mobs})

def laptop(request):
    laptops = Category.objects.get(category = 'Laptops')
    laps = Product.objects.filter(category=laptops)
    return render(request, 'laptop.html', {'laps':laps})

def cameras(request):
    camera = Category.objects.get(category = 'Camera')
    cams = Product.objects.filter(category = camera)
    return render(request, 'cameras.html', {'cams':cams})

def gadgets(request):  
    gadget = Category.objects.get(category = 'Gadgets')
    gads = Product.objects.filter(category = gadget)
    return render(request, 'gadgets.html', {'gads':gads})

@login_required(login_url = 'login')
def cart(request):
    cart = Cart.objects.filter(user = request.user)
    return render(request, 'cart.html', {'cart':cart})

def addtocart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pros_id = int(request.POST.get('product_id'))
            prod_check = Product.objects.get(id = pros_id)

            if(prod_check):
                if(Cart.objects.filter(user = request.user.id, product_id = pros_id)):
                    return JsonResponse({'status':"Product already in cart."})
                else:
                    prod_qty = int(request.POST.get('quantity'))

                    if prod_check.quantity >= prod_qty:
                        Cart.objects.create(user = request.user, product_id = pros_id, quantity = prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':"Only "+ str(prod_check.quantity) +" quantity available"})
            else:
                return JsonResponse({'status':"No such product available"})
        return redirect('/')
    else:
        return JsonResponse({'status':"Login to continue"})

def updatecart(request):
    if request.method == 'POST':
        pros_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user = request.user, product_id = pros_id)):
            prod_qty = int(request.POST.get('quantity'))
            cart = Cart.objects.get(product_id = pros_id, user = request.user)
            cart.quantity = prod_qty
            cart.save()
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        pros_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user = request.user, product_id = pros_id)):
            item = Cart.objects.get(product_id = pros_id, user = request.user)
            item.delete()
            return JsonResponse({'status': "Item Deleted"})
    return redirect('/')

@login_required(login_url = 'login')
def wishlist(request):
    wish = Liked.objects.filter(user = request.user)
    return render(request, 'wishlist.html', {'wish':wish})

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pros_id = int(request.POST.get('product_id'))
            prod_check = Product.objects.get(id = pros_id)

            if(prod_check):
                if(Liked.objects.filter(user = request.user.id, product_id = pros_id)):
                    return JsonResponse({'status':"Product already in wishlist."})
                else:
                    Liked.objects.create(user = request.user, product_id = pros_id)
                    return JsonResponse({'status':"Product added successfully"})
            else:
                return JsonResponse({'status': "No such product found!"})
        else:
            return JsonResponse({'status': "Login to continue"})
    else:
        return redirect('/')

def deletewishitem(request):
    if request.method == 'POST':
        pros_id = int(request.POST.get('product_id'))
        if(Liked.objects.filter(user = request.user, product_id = pros_id)):
            cart = Liked.objects.get(product_id = pros_id, user = request.user)
            cart.delete()
            return JsonResponse({'status': "Item Deleted"})
    return redirect('/')

@login_required(login_url = 'login')
def checkout(request):
    rawcart = Cart.objects.filter(user = request.user)
    for prod in rawcart:
        if prod.quantity > prod.product.quantity:
            Cart.objects.delete(id = prod.id)
    cart = Cart.objects.filter(user = request.user)
    total_price = 0
    for prod in cart:
        total_price = total_price + prod.product.offer_price * prod.quantity
    context = {'cart' : cart, 'total_price' : total_price}
    return render(request, 'checkout.html', context)

@login_required(login_url = 'login')
def buynow(request, prod_id):
    if(Product.objects.filter(id = prod_id)):
        prod = Product.objects.filter(id = prod_id).first()
        price = 2
        total = 0
        total = total + prod.offer_price + price
        if request.method == 'POST':
            quantity = int(request.POST.get('quantity'))
        else:
            quantity = 1
        context = {'prod' : prod, 'total' : total, 'quantity' : quantity}
    else:
        messages.error(request, "No such product found!")
        return redirect('/')
    return render(request, 'buynow.html', context)