from django.db import models
import uuid


class Profile(models.Model):
    name = models.CharField(max_length=150, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    profile_orders = models.ManyToManyField("ProfileOrder", related_name="RelatedProfile", verbose_name="ProfileOrder")

    def __str__(self):
        return self.name


class ProfileOrder(models.Model):
    profile = models.ForeignKey(Profile, related_name="RelatedOrder", verbose_name="user", on_delete=models.CASCADE)
    address = models.CharField(max_length=150, verbose_name="address", null=True, blank=True)
