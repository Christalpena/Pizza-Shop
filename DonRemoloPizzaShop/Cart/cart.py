class Cart:

    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] ={}
        #else:
        self.cart = cart

    def Product_list(self):
        products = []
        for key,value in self.cart.items():
            data =  key,value
            products.append(data)
        return products
            

    def add(self,product):
        if (str(product.name) not in self.cart.keys()):
            self.cart[product.name] = {
                'product_id':product.id,
                'name': product.name,
                'price': str(product.price),
                'quantity': 1
            }

        else:
            for key,value in self.cart.items():
                if key == str(product.name):
                    value['quantity'] = value['quantity']+1
                    break
        self.save_cart()

    def save_cart(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def delete(self,product):
        product.name = str(product.name)
        if product.name in self.cart:
            del self.cart[product.name]
            self.save_cart()

    def subtract_products(self, product):
        for key,value in self.cart.items():
            if key == str(product.name):
                value['quantity'] = value['quantity']-1

 
                if value['quantity']<1:
                    self.delete(product)
                break
        self.save_cart()

    def clean_car(self):
        self.session['cart'] = {}
        self.session.modified = True







        