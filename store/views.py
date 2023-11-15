from django.shortcuts import render,redirect
from . models import Product, Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.forms import SignUpForm



def home(request):
    products= Product.objects.all()
    return render (request,"home.html",{
        'products' : products
    })

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('You have been logged in'))
            return redirect("home")
        else:
            messages.success(request,('Invalid Credentials'))
            return redirect("login")
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out successfully'))
    return redirect("home")

def register_user(request):
    form= SignUpForm()
    if request.method=="POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1'] # don't worry abt pass2 django we'll do validation on it's own
            #log in user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('You are a newly registered user'))
            return redirect("home")
        else:
            messages.success(request,('Somrthing went wrong, please try again'))
            return redirect("register")
    else:
        return render(request,'register.html',{
            'form':form
        })

def product(request,pk):
    product= Product.objects.get(id=pk)
    return render (request,"product.html",{
        'product' : product
    })

def category(request,bak):
    #replace spalces with hyphens
    bak=bak.replace("-"," ")
    # get category from the url
    try:
        # look up the category
        category = Category.objects.get(name=bak)
        products = Product.objects.filter(category=category)
        return render (request,"category.html",{
            'products':products
        })
    except:
        messages.success(request,("Did'nt exist"))
        return redirect("home")
