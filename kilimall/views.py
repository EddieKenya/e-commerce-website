from django.shortcuts import render
from django.contrib import auth
from.models import *
from django.http import JsonResponse

# Create your views here.
def main(request):
    return render(request, 'main.html')

def store(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create( customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        
    context ={'items':items, 'order':order}
    return render(request,'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create( customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context ={'items':items, 'order':order}   
    return render (request, 'checkout.html', context)

def updateItem(request):
    return JsonResponse('Item was added', safe=False)