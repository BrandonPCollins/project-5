from django.shortcuts import render

def cart_summary(request):
    """ A view that renders the cart contents page """
    return render(request, "cart_summary.html")



def cart_add(request):
    pass 

def cart_delete(request):
    pass

def cart_update(request):
    pass 