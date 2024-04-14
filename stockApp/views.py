from django.shortcuts import render
from .models import Category ,Brand ,Sale ,Purchase
from rest_framework import viewsets
from .permissions import IsAuthenticatedAndWriteOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import CategorySerializer , BrandSerializer


def category_search(request):
    if 'name' in request.GET:
        name = request.GET['name']
        categories = Category.objects.filter(name__icontains=name)
    else:
        categories = Category.objects.all()
    return render(request, 'your_template.html', {'categories': categories})

def category_filter(request):
    if 'name' in request.GET:
        name = request.GET['name']
        categories = Category.objects.filter(name=name)
    else:
        categories = Category.objects.all()
    return render(request, 'your_template.html', {'categories': categories})

def brand_search(request):
    if 'name' in request.GET:
        name = request.GET['name']
        brands = Brand.objects.filter(name__icontains=name)
    else:
        brands = Brand.objects.all()
    return render(request, 'your_template.html', {'brands': brands})

def sale_search(request):
    if 'brand' in request.GET:
        brand = request.GET['brand']
        sale = Sale.objects.filter(brand__icontains=brand)
    else:
        sale = Sale.objects.all()
    return render(request, 'your_template.html', {'sale': sale})

def sale_filter(request):
    brand = request.GET.get('brand')
    product = request.GET.get('product')

    sale = Sale.objects.all()
    if brand:
        sale = sale.filter(brand=brand)
    if product:
        sale = sale.filter(product=product)

    return render(request, 'your_template.html', {'sale': sale})

def purchase_search(request):
    if 'firm' in request.GET:
        firm = request.GET['firm']
        purchase = Purchase.objects.filter(firm__icontains=firm)
    else:
        purchase = Purchase.objects.all()
    return render(request, 'your_template.html', {'purchase': purchase})

def purchase_filter(request):
    firm = request.GET.get('firm')
    product = request.GET.get('product')

    purchase = Purchase.objects.all()
    if firm:
        purchase = purchase.filter(firm=firm)
    if product:
        purchase = purchase.filter(product=product)

    return render(request, 'your_template.html', {'purchase': purchase})




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]



