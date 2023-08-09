from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models
# Create your views here.


def index(request):

    product_objects = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})



# class ProductDetail(DetailView):
#     context_object_name='product_detail'
#     model = models.Product
#     template_name = 'shop/product_detail.html'



def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', '')
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip = request.POST.get('zip', "")
        total = request.POST.get('total', "")

        order = Order(items=items, name=name, email=email, address=address,
                      city=city, state=state, zip=zip, total=total)
        order.save()

    return render(request, 'shop/checkout.html')



def detail(request, id):
    product_object = Product.objects.get(id=id)
    print(product_object.title)
    return render(request, 'shop/detail.html', {'product_object': product_object})