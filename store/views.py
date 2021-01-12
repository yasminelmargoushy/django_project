from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.db.models import Q
from .models import *
from blog.models import *
import random
from django.core.paginator import Paginator


def store (request):
    products = Product.objects.all().order_by('-date')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context ={'products':products}
    return render (request,'store/store.html',context)
    

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        postorder, created = PostOrder.objects.get_or_create(customer=customer,complete = False)
        postitems = postorder.postorderitem_set.all()
        totalitems = postorder.get_cart_items + order.get_cart_items
        total = postorder.get_cart_total + order.get_cart_total
    else:
        items = []
        postitems = []
        totalitems = 0
        total = 0
    context ={'items': items ,'postitems':postitems, 'total':total , 'totalitems':totalitems}
    return render (request,'store/cart.html',context)



def checkout(request):
    context ={}
    return render (request,'store/checkout.html',context)

def updateitem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('productId:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=  0:
        orderItem.delete()

    return JsonResponse ('Item was added', safe=False)

def search(request):
    kw = request.GET.get('keyword')
    products = Product.objects.filter(Q(name__icontains=kw) | Q(description__icontains=kw))
    context = {
        'products': products
    }
    print(products)
    return render (request,'store/search.html', context)


def product(request,id):

    product = Product.objects.get(pk=id)
   
    # Add review
    related_products = list(Product.objects.filter(category=product.category).exclude(id=product.id))
    
    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)

    imagesstring = "{'image': '%s'}," % ( product.image.url)
    category_products= list(Product.objects.filter(category=product.category))
    imagesstring = "{'image': '%s'}," % ( product.image.url)
    context= {'product':product,
              'related_products':related_products,
              'category_products':category_products}
    return render(request, "store/product.html", context)
    product.save()


def productreview(request,id):
        product = Product.objects.get(pk=id)
        related_products = list(Product.objects.filter(category=product.category).exclude(id=product.id))
    
        if len(related_products) >= 3:
            related_products = random.sample(related_products, 3)

        imagesstring = "{'image': '%s'}," % ( product.image.url)
        context= {'product':product,
                   'related_products':related_products}
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')
        date_added= request.POST.get('date_added', '')
        review = ProductReview.objects.create(product=product, stars=stars, content=content,date_added=date_added)
        return render(request, "store/product.html", context)
        review.save()
        return redirect('product')


def Category (request):
    products = Product.objects.all
    category_products= list(Product.objects.filter(category=request.POST.get('Category')))
    #imagesstring = "{'image': '%s'}," % ( product.image.url)
    context= {'product':product,
              'category_products':category_products}
    return render (request,'store/store.html',context)

