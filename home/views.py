from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout


# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact_us(request):
    return render(request, 'home/contact.html')
 

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        params={}
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            return HttpResponse('Please fill the form correctly')
            

        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
    return render(request, "home/contact.html")
    
def signuppage(request):
    return render(request, 'home/signup.html')

def signup(request):
    if request.method == "POST":
        # Get the POST parameters
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        if pass1==pass2:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request, 'home/signup.html')
            except User.DoesNotExist:
                myuser= User.objects.create_user(username= username, password= pass1, email= email, first_name= fname, last_name= lname)
                myuser.save()
                return redirect("home")


           
    else:
        return HttpResponse('This is not allowed')

def login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user= authenticate(username= loginusername, password= loginpassword)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return redirect('/')
    return HttpResponse("404 - Not Found post")
    

