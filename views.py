from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from . models import AbstractBaseUser,usermodel,usermodel1
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from datetime  import datetime


# function to render any page
def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def help(request):
    return render(request,'help.html')

# if user is authenticated(logged in with correct information) 
# then redirect it to home page
# else redirect user to login page

def home(request):
    # print(request.user)
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('/login')

# function for logout user
def logoutUser(request):
    logout(request)
    return redirect('/login')

# function for login user
def loginUSER(request):
    if request.method == 'POST':
        username = request.POST.get('username1')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request,'Please Enter Correct Username Or Password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


# function create account
# it will create User As Well as model in your backend
# as you can below there are user.save() and user1.save()
# user.save() is used to avoid anonymous user error and
# user.save1() is used to save imformation in your backend

def signup(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if not username or not  email or not  password or not  confirmpassword :
            messages.error(request,'Please Fill Form Correctly')
            return render(request,'signup.html')
        elif password != confirmpassword :
            messages.error(request,'Your Password Does Not Match')
            return render(request,'signup.html')
        
        # to check if user is already is exist
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exist')
            return render(request,'signup.html')
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        user1 = usermodel(username=username, password=password, email=email ,confirmpassword=confirmpassword)
        user1.save()
        messages.success(request,'Account Created Successfully')
        return redirect('/login')
    else :
        return render(request,'signup.html')




# basic funstion to save your model in backend(admin)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email1 = request.POST.get('email1')
        message = request.POST.get('message')
        model = usermodel1(name=name, email1=email1 , message=message)
        model.save()
    return render(request,'contact.html')



