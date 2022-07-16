from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket

# Functions
def basket_summary(request):
    return render(request, 'store/basket/summary.html',)

def basket_add(request):
    basket = Basket(request) #session data collection here
    if request.POST.get('action') == 'post': #if statment: to check its a post
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)#find prod in DB
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

