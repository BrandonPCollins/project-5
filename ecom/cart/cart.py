
class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get current session if it exists
        cart = self.session.get('session_key')

        #If new user, create session!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #Ensure cart is available on all pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True