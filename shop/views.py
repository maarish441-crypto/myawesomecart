from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil



def index(request):
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))

    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds} 
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) + (n//4))
        allProds.append([prod,range(1,nSlides),nSlides])



    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return  render(request,'shop/about.html')

def contact(request):
    return HttpResponse('contact')

def tracker(request):
    return HttpResponse('tracker')

def search(request):
    return HttpResponse('search')

def prodView(request):
    return HttpResponse('prodView')

def checkout(request):
    return HttpResponse('checkout')


