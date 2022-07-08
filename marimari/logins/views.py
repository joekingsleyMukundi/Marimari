from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


        

def about(request):
    return render(request,"about.html")
   
def home(request):
    return render (request,"home.html")

def verification(request):
    return render (request,"verification.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")

    else:
        form = UserCreationForm()
    return render(request,"register.html", {"form":form})

# def registerCustomer(request):
#     forms =CustomersForm()
#     if request.method == 'POST':
#         form = CustomersForm(request.POST)
#         if form.is_valid():
#           form.save()      
#         return HttpResponseRedirect("staff/signin/")


def signin(request):
    if request.method == "POST":
        form_data=request.POST
        username = form_data['username']
        password = form_data['password']  
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
                user = authenticate(username=username, password=password)
                login(request, user)
                print("DATA USERNAME={} PASSWORD={}".format(username, password))
            
                return redirect('/store/index/')
           
    else:
        form = AuthenticationForm()
    return render(request,"signin.html", {"form":form})

def signout(request):
    logout(request)
    return HttpResponseRedirect("/store/index/")