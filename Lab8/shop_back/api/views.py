from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from .models import Product , Category
from rest_framework import status


# Create your views here.


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id = id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error" : "Product not found"}, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['Get'])
def products_by_category(request, id):
    try:
        category = Category.objects.get(id = id)
        products = Product.objects.filter(category = category)
        serializer = ProductSerializer(products,many =True)
        return Response(serializer.data)
    
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status = status.HTTP_404_NOT_FOUND)
    