from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "GET":
       return render(request,'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('ja existe')
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()

        return HttpResponse('User cadastrado com sucesso')




def login_user(request):
    if request.method == "GET":
       return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(username=username,password=password) 
        
        if user is not None:
            login(request,user)
            return HttpResponse('Sucesso')
        else:
            return HttpResponse('Erro')
        

@login_required(login_url='/auth/login/')          
def plataforma(request):
    return HttpResponse('Plataforma')



def logout_user(request):
    logout(request)
    return HttpResponse('Logout sucesso')
    