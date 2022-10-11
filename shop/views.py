import json
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from .models import Order, Product, Contact, OrderUpdate

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

def searchMatch(query, item):
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.subcategory.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    products = Product.objects.all()
    # print(products)
    n = len(products)


    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    print(cats)
    for cat in cats:  
        prodTemp = Product.objects.filter(category=cat)
        prod = [item for item in prodTemp if searchMatch(query,item)]

        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        if len(prod) !=0:
            allProds.append([prod, range(1, nSlides), nSlides])   

    params = {'allProds': allProds, "msg":""}
    if(len(query)< 4 | len(allProds) == 0):
        params = {'msg':"Please make sure to enter relevant search querry"}
    return render(request, 'shop/search.html', params)


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
        thank = True
        return render(request, 'shop/contact.html', {'thank':thank})


    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status": "success", "updates":updates, "itemsJson":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "noItem"}')
        except Exception as e:
            return HttpResponse('{"status": "error"}')

    return render(request, 'shop/tracker.html')

def prodView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html', {'product':product[0]});

def checkOut(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        items_json = request.POST.get('itemsJson', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(items_json=items_json, name=name, email=email, phone=phone, state=state, zip_code=zip_code, city=city, address=address)
        order.save();
        id = order.order_id
        thank = True
        update = OrderUpdate(order_id = order.order_id, update_desc="Your Order has been placed")
        update.save();
        return render(request, 'shop/checkOut.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkOut.html')
