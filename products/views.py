from django.shortcuts import render
from products.models import Product
from django.shortcuts import get_object_or_404

def index(request):
  products = Product.objects.all().order_by('name') #in order
  context = {'products': products} #still in order
  response = render(request, 'products/index.html', context)
  return response 

def show(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  context = {'products': product} #still in order
  response = render(request, 'products/show.html', context)
  return response 
