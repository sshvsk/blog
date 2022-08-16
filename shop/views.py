from django.db.models import Sum, F
from django.http import HttpResponse

from shop.models import Product, Purchase
from shop.services import get_sorted_product


def products(request):
    if request.GET.get('color'):
        product_list = Product.objects.filter(color=request.GET.get('color'))
    else:
        product_list = Product.objects.all()
    order_by = request.GET.get('order_by')

    product_list = get_sorted_product(product_list, order_by)
    return HttpResponse(", ".join([x.title for x in product_list]))


def purchases(request):
    Purchase.objects.annotate(purchase_count=Sum(F("count") * F("product__cosert"))).values('product')