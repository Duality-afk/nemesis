from django.core.checks import messages
from django.shortcuts import redirect, render
from home import serializers
from home.models import Account
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout
from django.contrib import messages
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
import uuid
from home.serializers import RegistrationSerializer


# Create your views here.
def loginpage(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("success!")
            return redirect("/")
        else:
            messages.warning(request,'Please enter valid credentials!')
            return redirect("/login")
    else:
        return render(request, "login.html")


def registerpage(request):
    if request.method == "POST":
  
        email = request.POST.get('email')
        if Account.objects.filter(email=email).exists():
            messages.warning(request,'email already exists')
            return redirect("/register")
        username = request.POST.get('username')
        if Account.objects.filter(username=username).exists():
            messages.warning(request,'username already exists')
            return redirect("/register")
        address =request.POST.get('address')
        password = request.POST.get('password')
        password1 = request.POST.get('confirmpassword')
        

        user = Account.objects.create_user(email=email, username=username,password=password,address=address)
        user.save()
        print("Data successfully added")
    return render(request,"register.html")


'''class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return render(request,"login.html")

        return render(request,"login.html")'''
        



def dashboard(request):
    if request.user.is_authenticated:
        userdetails = Account.objects.get(username=request.user.username)
        email = userdetails.email
        username = userdetails.username
        address  = userdetails.address
        value = request.POST.get('value')
        print(value)
        edituserEmail = "inactive"
        edituserAdd = "inactive"
        edituserUsername = "inactive"
        if value == "TrueEmail":
            edituserEmail = "active"
        if value == "TrueUsername":
            edituserUsername = "active"
        if value == "TrueAddress":
            edituserAdd = "active"
        


        context = {
            "email":email,
            "username":username,
            "address":address,
            "edituserEmail":edituserEmail,
            "edituserUsername":edituserUsername,
            "edituserAdd":edituserAdd,

        }
        return render(request,"dashboard.html",context)
    else:
        return render(request, "dashboard.html")


def update(request):
    if request.method=="POST":
        userdetails = Account.objects.get(email=request.user)
        value = request.POST['value']
        if value == "username":
            userdetails.username = request.POST.get('username')
            if Account.objects.filter(username=userdetails.username).exists():
                messages.warning(request,'username already exists')
            else:
                userdetails.save()
        if value == "address":
            userdetails.address = request.POST.get('address')
            userdetails.save()
        if value == "email":
            userdetails.email = request.POST.get('email')
            if Account.objects.filter(email=userdetails.email).exists():
                messages.warning(request,'email already exists')
            else:
                userdetails.save()
        return redirect("/")


def delete(request):
    if request.method == "POST":
        userdetails = Account.objects.get(username=request.user.username)
        value = request.POST.get('value')
        if value == "address":
            userdetails.address = ""
            userdetails.save()
        if value == "username":
            userdetails.username = ""
            userdetails.save()
        
        if value == "email":
            userdetails.delete()


        return redirect('/')


def handlelogout(request):
    logout(request)
    return redirect("/")