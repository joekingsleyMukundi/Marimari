from django.shortcuts import render
from staff.models import *
# Create your views here.
# @login_required
def account(request):
    category = Category.objects.all()
    context = {
        'categories': category,
    }
    
    return render(request,"account.html" , context)