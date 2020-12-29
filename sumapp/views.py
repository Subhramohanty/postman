from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.urls import reverse_lazy


# Create your views here.
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ProductList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class CategoryList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class OrderList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field='id'



