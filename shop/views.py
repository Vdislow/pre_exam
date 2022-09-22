from django.shortcuts import render
from django.db import IntegrityError
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Item, Category, Order
from account.models import Profile
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer
from .permissions import IsAuthorPermission, ItemRUDPermission, OrderPermission


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorPermission, ]


class ItemView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return self.queryset.filter(category_id=self.kwargs['category_id'])

    def perform_create(self, serializer):
        serializer.save(
            category=get_object_or_404(Category, id=self.kwargs['category_id']),
            profile=self.request.user.profile
        )


class ItemRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [ItemRUDPermission, ]


class OrderListCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [OrderPermission, ]

    def perform_create(self, serializer):
        serializer.save(
            item=get_object_or_404(Item, id=self.kwargs['pk']),
            profile=self.request.user.profile
        )


class OrderRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [OrderPermission, ]

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs['pk'])
