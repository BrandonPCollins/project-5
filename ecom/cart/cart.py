class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get current session if it exists
        cart = self.session.get('session_key')

        #If new user, create session!
        if 'session_key' is not in request.session:
            cart = self.session['session_key'] = {}

        #Ensure cart is available on all pages
        self.cart = cart