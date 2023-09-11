from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from math import ceil

def index(request):
    allProds = []
    catprods = Product.objects.values('category','product_id')
    cats = {item['category'] for item in catprods}
    print(catprods,'\n',cats)
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}


    return render(request, 'index.html',params)

def index2(request,cat):
    
    catprods = Product.objects.filter(category=cat)

    params = {'prod':catprods}


    return render(request, 'index2.html',params)

def view(request,id):

    view_prod = Product.objects.get(product_id=id)

    params = {'prod':view_prod}

    return render(request,'viewProd.html',params)

def base(request):

    return render(request,'base.html')

def home(request):
    
    return HttpResponse('hellooo guysss kese ho')

def my_bag(request):

    all = Product.objects.all()

    params = {'all':all}

    return render(request, 'myBag.html',params)