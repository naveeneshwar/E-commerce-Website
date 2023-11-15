from .cart import Cart

#Create context processor so the cart works on all pages of the site

def cart(request):
    #return the default data from the cart
    return {'cart': Cart()}