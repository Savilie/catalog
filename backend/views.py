from django.shortcuts import render
from rest_framework import status, permissions, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import *

class ProductApiView(APIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()  # Установите queryset вашей модели Product

    def get(self, request):
        products = Product.objects.all()

        return Response(ProductSerializer(products, many=True).data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
