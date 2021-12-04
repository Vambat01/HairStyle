from django.urls import path
from .views import *

app_name = "Comment"
urlpatterns = [path("comments/", CommentListView.as_view())]
# path("comments/", CommentDetail.as_view())]
