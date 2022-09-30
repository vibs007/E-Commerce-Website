from heapq import nsmallest
from unicodedata import category
from django.shortcuts import render
from .models import Product, Contact

# Create your views here.
from django.http import HttpResponse
from .models import Product
from math import ceil, prod

def index(request):
    products = Product.objects.all()
    # print(products)
    n = len(products)

    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])   

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
   return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        date = request.POST.get('date', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        contact.save();


    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def prodView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html', {'product':product[0]});

def checkOut(request):
    return render(request, 'shop/checkOut.html')
