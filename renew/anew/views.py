# from pyexpat.errors import messages
from django.contrib import messages

from urllib import request
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect, render


def signout(request):
    logout(request)
    # messages.success(request, "Logged Out Successfully!!")
    return redirect('login')


def login_view(request):
    if 'username' in request.session:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            fname = username
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/home.html",{"fname":fname})
        else:
            
           messages.error(request, "wrong details!!")
           
                # messages.error(request, "wrong password!!")
           return redirect('login')

    return render(request,"authentication/login.html")


def home_view(request):
    if 'username' in request.session:

        return render(request,"authentication/home.html")
    
    return redirect('login ')