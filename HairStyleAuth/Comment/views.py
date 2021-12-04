from django.shortcuts import get_object_or_404
from rest_framework import pagination, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100

    def get_queryset(self):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('comment_id'))
        return comment.commentitem.all()

