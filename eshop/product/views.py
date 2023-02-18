from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer

from .models import Product

# Create your views here.

@api_view(['GET'])
def get_products(request):

    products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)

    return Response({ "products": serializer.data })


@api_view(['GET'])
def get_product(request, pk):

    product = get_object_or_404(Product, id=pk)

    serializer = ProductSerializer(product, many=False)

    return Response({ "product": serializer.data })