from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


def signup(request):
    if request.method == "POST":
        # to create a user
        if request.POST['password'] == request.POST['passwordagain']:
            # if both password match
            # check if user exits
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'registration.html', {'error': "username already exits"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
                return redirect(login)
        else:
            return render(request, 'registration.html', {'error': "password dont match"})


    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        # if a user exits or not with user name or password
        uname = request.POST['username']
        pwd = request.POST['password']
        user= auth.authenticate(username=uname,password=pwd)
        if user is not None :
            auth.login(request,user)
            return render(request,'index.html')
        else:
            return render(request, 'login.html', {'error': "invalid login"})
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'home.html')