from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework import generics, pagination

from rest_framework.generics import GenericAPIView, get_object_or_404


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Order.objects.none()
        return user.order.all()


def auth(request):
    return render(request, 'oauth.html')

    # Подключить юзера к ордеру
    # И проверка на реквест ужаления всего и защита от удаление.
    # Нажимать не кнопками, а реквестами


class OrderItemList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100

    def get_queryset(self):
        order = get_object_or_404(Order, pk=self.kwargs.get('order_id'))
        return order.orderitem.all()
