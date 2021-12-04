from django.db import models
from Profile.models import Profile


class Comment(models.Model):
    GRADES = (
        (0, 'Low'),
        (1, 'Normal'),
        (2, 'High'),
    )
    profile_id = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    comment_body = models.CharField(max_length=350, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(default=1, choices=GRADES)

    def __str__(self):
        return self.comment_body


class CommentItem(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.PROTECT, related_name='commentitem')
    comment_body = models.CharField(max_length=350, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(default=1)
