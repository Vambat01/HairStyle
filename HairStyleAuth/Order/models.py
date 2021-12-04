import uuid
from django.db import models
from Comment.models import Comment
from Profile.models import Profile


class Order(models.Model):
    profile_id = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    comment_id = models.OneToOneField(Comment, null=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=30, editable=True)
    order_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Status:
        new = 'New order'
        processing = 'Order processing'
        finished = 'Finished'

    status_list = [
        (Status.new, 'New order'),
        (Status.processing, 'Order processing'),
        (Status.finished, 'Finished'),
    ]
    order_status = models.CharField(max_length=100, default=Status.new, choices=status_list)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT, related_name='orderitem')
    amount_of_items = models.PositiveSmallIntegerField(default=1)
