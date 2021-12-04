from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.Serializer):
    comment_body = serializers.CharField(max_length=350)
    date_of_creation = serializers.DateTimeField()
    grade = serializers.IntegerField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment_body = validated_data.get('comment_body', instance.comment_body)
        instance.date_of_creation = validated_data.get('date_of_creation', instance.date_of_creation)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance