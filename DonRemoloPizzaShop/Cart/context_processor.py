
from Cart.cart import Cart


def import_total_cart(request):
    cart = Cart(request)

    total=0

    for key,value in request.session['cart'].items():
        total= total+(float(value['price'])*value['quantity'])


    return {'import_total_cart':total}

        