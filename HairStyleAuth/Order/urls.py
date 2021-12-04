from django.urls import path
from .views import *

app_name = "Order"
urlpatterns = [path("orders/", OrderListView.as_view()),
               path('orderitems/', OrderItemList.as_view())]
