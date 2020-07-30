from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages

# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/products')
            # A backend authenticated the credentials
        else:
            messages.warning(request, 'Wrong username or password!')
            return redirect("/login")
            # return render(request,'login.html')
            # No backend authenticated the credentials
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

def products(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'products.html')