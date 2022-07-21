from .basket import Basket



#this will make the basket available in all pages
def basket(request):
    return {'basket': Basket(request)}