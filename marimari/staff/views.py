
from django.shortcuts import redirect, render   
from .models import *
from django.http import HttpResponse , HttpResponseRedirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.decorators.http import require_http_methods

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")
    
# def registerCustomer(request):
#     forms =CustomersForm()
#     if request.method == 'POST':
#         form = CustomersForm(request.POST)
#         if form.is_valid():
#             form.save()      
#         return HttpResponseRedirect("staff/signin/")
      
# def customers(request):
#     context = {
#         'form': CustomersForm()
#     }
#     return render(request, 'register.html', context)
# # @require_http_methods(["POST"])       
# def signin(request):
#     form_data=request.POST
#     username = form_data['username']
#     password = form_data['password']   
#     # if user:
#     #     login(request, user)
#     #     return HttpResponse("OK")
#     # else:
#     #     return HttpResponse("Unauthorized", status=401)
#     return HttpResponse(username, password)



# def signin(request):
#     if request.method == "POST":
#       form = AuthenticationForm(data = request.POST)
#       if form.is_valid():
#             form_data=request.POST
#             username = form_data['username']
#             password = form_data['password']
            
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             print("DATA USERNAME={} PASSWORD={}".format(username, password))
            
#             return redirect('/store/index/')
#     else:
#         form = AuthenticationForm()
#     return render(request, "signin.html", {"form":form})

# def signout(request):
#     logout(request)
#     return HttpResponseRedirect("store/index/")

