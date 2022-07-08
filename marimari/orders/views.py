from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render,  HttpResponseRedirect,redirect
from store.views import product_details
from staff.models import *
from django.contrib import messages
from django.db.models import Count, Avg, F, Sum
from django.db.models import Q
from django.views import View
from django.contrib.auth import models

# Create your views here.
def view(request):
  response = HttpResponse('device')
  response.set_cookie('device', 'cookie_value')


def add_to_wishlist(request, id):

    user_id = request.user.id
    product = get_object_or_404(Product, id=id)
    if product.user_wishlist.filter(id=user_id).exists():
        product.user_wishlist.remove(request.user)
        # messages.success(item has been removed from your wishlist")
    else:
        product.user_wishlist.add(request.user)  
        # messages.success(item has been added to your wishlist")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def wishlist(request):
    product = Product.objects.all()    
    category = Category.objects.all()
    products = Product.objects.filter(user_wishlist=request.user)
    product_id = Product.objects.filter(user_cart=request.user)
    total = product_id.aggregate(data=Sum('product_cost'))
    discounts = product_id.aggregate(discounts=Sum('discounts'))

    context = {
         "products": product,
        'categories': category,
        "wishlist":products,
        'cart_products':product_id,
        'discounts':discounts,
        'sum_data':total,
        }
    return render(request, "wishlist.html", context)

def add_to_cart(request, id): 
    user_id = request.user.id
    product = get_object_or_404(Product, id=id)
    
    if product.user_cart.filter(id=user_id).exists():
        product.user_cart.remove(request.user)
        # messages.success(item has been removed from your cart")
    else:
        product.user_cart.add(request.user)  
        # messages.success(item has been added to your cart")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])    
    
def cart(request):
    if request.method != 'POST':  
        product = Product.objects.all()  
        category = Category.objects.all()  
        product_id = Product.objects.filter(user_cart=request.user)
        products = Product.objects.filter(user_wishlist=request.user)
        total = product_id.aggregate(data=Sum(F('product_cost')- F('discounts')))
        discounts = product_id.aggregate(discounts=Sum('discounts')) 
        
        
        context = {
        "products": product,
        'sum_data':total,
        'discounts':discounts,     
        "cart_products": product_id,
        "wishlist":products,
        'categories': category, 
            }
        
        
        return render(request, 'cart.html', context) 
    else:
        quantity = int(request.POST['quantity_field'])  
        prod_id = int(request.POST['product-id'])
        if quantity and prod_id: 
            product = Product.objects.all()  
            product_id = Product.objects.filter(user_cart=request.user)
            total = product_id.aggregate(data=Sum(F('product_cost')- F('discounts')))
            discounts = product_id.aggregate(discounts=Sum('discounts'))
            
            context = {  
            "products": product,
            'product_qty':quantity,         
            'sum_data':total,
            "cart_products": product_id,
                }
            
            
            return render(request, 'cart.html', context) 
     
     
   
    

