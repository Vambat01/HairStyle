from django.urls import path

from Order.views import OrderItemList

from .views import *

app_name = "Profiles"
urlpatterns = [
    path("profiles/", ProfileList.as_view()),
    path("profiles/<str:pk>", ProfileDetail.as_view()),

    path("profiles/<str:pk>/orderitems/", OrderItemList.as_view())

]
