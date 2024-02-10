from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    """ A view that renders the cart contents page """
    return render(request, "cart_summary.html")

def cart_add(request):
    cart = Cart(request)
    #Test for Post
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        #Grab product in database
        product = get_object_or_404(Product, id=product_id)
        #Save to session
        cart.add(product=product)

        #Cart Quantity
        cart_quantity = cart.__len__()
        #Return Response
        #response = JsonResponse({'Product Name: ' : product.name})
        response = JsonResponse({'qty:' : cart_quantity})
        return response 

def cart_delete(request):
    pass

def cart_update(request):
    pass 