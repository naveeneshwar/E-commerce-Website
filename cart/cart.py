#sessions
class Cart():
    def __int__(self, request):
        self.session = request.session
   
    #get's the current session key if exists
        cart = self.session.get("session_key")
        
        # if new user i.e no session_key, create one

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # makeing sure cart is available on all pages of the site

        self.cart = cart

