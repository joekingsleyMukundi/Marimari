from itertools import product
from sys import setswitchinterval
from urllib import request
from django.views import View
from staff.models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView , DetailView


app_name="categories"

# Create your views here.
class SearchResultsView(ListView):
    model = Product
    template_name = "search.html"
    def get_queryset(self):  # new
        query = self.request.GET["search_value"]
        category = int(self.request.GET["category"])
        
        
        if category == 0:
            object_list = Product.objects.all()
        
        if query and not category:
            object_list = Product.objects.filter(
                Q(product_name__icontains=query)
            )
        elif category and not query:
            object_list = Product.objects.filter(
                Q(category__id=category)
            )
            
        else:
            object_list = Product.objects.filter(
                Q(category__id=category), Q(product_name__icontains=query)
            )
      
        return object_list
    
    def get_context_data(self,*args, **kwargs):
        context = super(SearchResultsView, self).get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
class CategoryView(View):
    def get(self, request, id):
        category = Category.objects.filter(id=id).first()
        products = Product.objects.filter(category=category)

        context ={
            'categories':category,
            'products':products,
         }
        return render(request, 'categories.html', context)
   
def searchFilter(request):  
    if request.user.is_authenticated: 
        category = Category.objects.all() 
        min_price = request.GET['min-price']
        max_price = request.GET['max-price']
        productsFilter = Product.objects.filter(product_cost__range=(min_price, max_price))
        product_id = Product.objects.filter(user_cart=request.user) 
        total = product_id.aggregate(data=Sum(F('product_cost')-F('discounts')))
        products = Product.objects.filter(user_wishlist=request.user)
        context = {
                'categories':category,
                'min_price': min_price,
                'max_price': max_price,
                'object_list': productsFilter, 
                "cart_products": product_id,  
                'sum_data':total,
                "wishlist":products,     
            }
        
        return render(request, 'search.html', context)
    else:
        category = Category.objects.all() 
        min_price = request.GET['min-price']
        max_price = request.GET['max-price']
        productsFilter = Product.objects.filter(product_cost__range=(min_price, max_price))
        context = {
                'categories':category,
                'min_price': min_price,
                'max_price': max_price,
                'object_list': productsFilter, 
            }
        
        return render(request, 'search.html', context)

    
def one(request):
    if request.user.is_authenticated:
        category = Category.objects.all() 
        products = Product.objects.filter(user_wishlist=request.user)
        product_id = Product.objects.filter(user_cart=request.user) 
        price = Product.objects.filter(product_cost__lte = 10000)
        context={
            "cart_products": product_id,  
            'categories':category,
            "wishlist":products,  
            "object_list":price
        }
        return render(request,'search.html', context) 
    else:
        category = Category.objects.all() 
        price = Product.objects.filter(product_cost__lte = 10000)
        context={
            'categories':category,
            "object_list":price
        }
        return render(request,'search.html', context) 
    
def two(request):
    if request.user.is_authenticated:
        category = Category.objects.all() 
        products = Product.objects.filter(user_wishlist=request.user)
        product_id = Product.objects.filter(user_cart=request.user) 
        price = Product.objects.filter(product_cost__gt = 10000, product_cost__lte = 50000)
        context={
            "cart_products": product_id,  
            'categories':category,
            "wishlist":products, 
            "object_list":price
        }
        return render(request,'search.html', context) 
    else:
        category = Category.objects.all() 
        price = Product.objects.filter(product_cost__gt = 10000, product_cost__lte = 50000)
        context={
            'categories':category,
            "object_list":price
        }
        return render(request,'search.html', context) 
    
def three(request):
    if request.user.is_authenticated:
        category = Category.objects.all() 
        products = Product.objects.filter(user_wishlist=request.user)
        product_id = Product.objects.filter(user_cart=request.user) 
        price = Product.objects.filter(product_cost__gt = 50000, product_cost__lte = 100000)
        context={
            "cart_products": product_id,  
            'categories':category,
            "wishlist":products,
            "object_list":price
        }
        return render(request,'search.html', context) 
    else:
        category = Category.objects.all() 
        price = Product.objects.filter(product_cost__gt = 50000, product_cost__lte = 100000)
        context={
            'categories':category,
            "object_list":price
        }
        return render(request,'search.html', context) 
         
    
def four(request):
    if request.user.is_authenticated:
        category = Category.objects.all() 
        products = Product.objects.filter(user_wishlist=request.user)
        product_id = Product.objects.filter(user_cart=request.user) 
        price = Product.objects.filter(product_cost__gt = 100000, product_cost__lte = 150000)
        context={

            "cart_products": product_id,  
            'categories':category,
            "wishlist":products,
            "object_list":price
        }
        return render(request,'search.html', context) 
    else:
        category = Category.objects.all() 
        price = Product.objects.filter(product_cost__gt = 100000, product_cost__lte = 150000)
        context={
            'categories':category,
            "object_list":price
        }
        return render(request,'search.html', context) 
    
def five(request):
    if request.user.is_authenticated:
        category = Category.objects.all() 
        products = Product.objects.filter(user_wishlist=request.user)
        product_id = Product.objects.filter(user_cart=request.user) 
        price = Product.objects.filter(product_cost__gt = 150000)
        context={
            "cart_products": product_id,  
            'categories':category,
            "wishlist":products,
            "object_list":price
        }
        return render(request,'search.html', context) 
    else:
        category = Category.objects.all() 
        price = Product.objects.filter(product_cost__gt = 150000)
        context={
            'categories':category,
            "object_list":price,
        }
        return render(request,'search.html', context) 
    
def categoryNav(request, id):
    category = Category.objects.all()
    name = Category.objects.filter(id=id)
    context = {
        'cat':name,
        'categories':category,
    }
    return render(request,'search.html', context) 
    




   
    
   
