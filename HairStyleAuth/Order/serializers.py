from rest_framework import serializers
from .models import OrderItem, Order


class OrderSerializer(serializers.ModelSerializer):
    # make all fields readonly
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'user', 'order_date', 'order_cost',
            'order_payment', 'order_shipment', 'order_status',
        ]

    def create(self, *args, **kwargs):
        print('here!')
        # return Order.create_order(self.context['request'].user)
        return super().create(*args, **kwargs)

    def update(self, instance, validated_data):
        print(1)
        instance.order_number = validated_data.get('order_number', instance.order_number)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.paid = validated_data.get('paid', instance.paid)
        instance.save()
        return instance
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'amount_of_items']