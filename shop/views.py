from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from . import product_data

# Create your views here.
def shop(request):
    searched_product= request.GET['search']
    product_data.data(searched_product)
    return render(request, 'shop/products.html')