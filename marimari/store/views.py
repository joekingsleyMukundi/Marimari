import json
from venv import create
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from staff.models import *
# from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        product = Product.objects.all()
        category = Category.objects.all()
        context = {
            'categories': category,
            "products": product,
                }
        return render(request, "index.html", context)
    else: 
        product = Product.objects.all()
        category = Category.objects.all()
        products = Product.objects.filter(user_wishlist=request.user)
        product_id = Product.objects.filter(user_cart=request.user)
        total = product_id.aggregate(data=Sum(F('product_cost')-F('discounts')))
        
        context = {
            "wishlist":products,
            "cart_products":product_id,
            'sum_data':total,
            'categories': category,
            "products": product,
                }
    
    return render(request, "index.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.add()           
        category = Category.objects.all()
        context = {
            'categories': category,
        }
    
    return render(request,"checkout.html", context)

def product_details(request, id): 
    if request.user.is_authenticated: 
        product = Product.objects.all()  
        category = Category.objects.all()
        product_images = ProductImage.objects.filter(product__id=id).first()
        product_detail = Product.objects.filter(id=id).first()
        products = Product.objects.filter(user_wishlist=request.user)
        product_id = Product.objects.filter(user_cart=request.user)
        total = product_id.aggregate(data=Sum((F('product_cost'))-F('discounts')))  
            
            
            
        context = {
                    "cart_products":product_id,
                    'sum_data':total,
                    "wishlist":products,
                    'categories': category,
                    "data":product_images,
                    "product": product_detail,
                    "products": product,
                }
        return render(request, "details.html" , context) 
    else:
        category = Category.objects.all()
        product = Product.objects.filter(id=id).first()
        product_images = ProductImage.objects.filter(product__id=id).first()
       
        context = {
                'categories': category,
                "data":product_images,
                "product": product,
            }
        return render( request, 'details.html', context)



