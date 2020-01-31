import datetime
import logging
import traceback
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import ValidationError
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from main.consts import validation_messages
from main.bd_divisions import DIVISION_CHOICES, DISTRICT_CHOICES, UPAZILA_CHOICES


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_store_login_access(sender, instance, created, **kwargs):
    if created:
        Store.objects.create(user=instance)
    # instance.store.save()


@receiver(post_save, sender=User)
def create_delivery_boy_login_access(sender, instance, created, **kwargs):
    if created:
        DeliveryBoy.objects.create(user=instance)
    # instance.deliveryboy.save()


class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store')
    store_name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=12)
    business_name = models.CharField(max_length=50, null=True, blank=True)
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    upazila = models.CharField(max_length=20, choices=UPAZILA_CHOICES)
    business_address = models.CharField(max_length=50)
    nid_number = models.CharField(max_length=20)
    verification = models.FileField(upload_to='disk/seller/%Y/%m/%d/')

    def __str__(self):
        return self.store_name

    def __repr__(self):
        return self.store_name

    def validate_unique(self, *args, **kwargs):

        super(Store, self).validate_unique(*args, **kwargs)
        sn_qs = self.__class__._default_manager.filter(store_name=self.store_name).exists()
        cn_qs = self.__class__._default_manager.filter(contact_number=self.contact_number).exists()
        if sn_qs:
            raise ValidationError(validation_messages.get("DUPLICATE_STORE"))
        if cn_qs:
            raise ValidationError(validation_messages.get("DUPLICATE_NUMBER"))

    def clean(self, *args, **kwargs):
        if self.store_name:
            self.store_name = self.store_name.lower()

    def save(self, *args, **kwargs):
        super(Store, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Store Manager")
        verbose_name_plural = _("Store Managers")


class DeliveryBoy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_boy')
    name = models.CharField(max_length=30, null=True, blank=True)
    number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    upazila = models.CharField(max_length=20, choices=UPAZILA_CHOICES)
    address = models.CharField(max_length=50)
    nid_number = models.CharField(max_length=20)
    verification = models.FileField(upload_to='disk/delivery_man/%Y/%m/%d/')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def validate_unique(self, *args, **kwargs):
        super(DeliveryBoy, self).validate_unique(*args, **kwargs)
        # qs = self.__class__._default_manger.filter(number=self.number).exists()
        qs = DeliveryBoy.objects.filter(number=self.number).exists()
        if qs:
            raise ValidationError(validation_messages.get("DUPLICATE_NUMBER"))

    class Meta:
        verbose_name = _("Delivery Boy")
        verbose_name_plural = _("Delivery Boys")


class Task(models.Model):
    ON_DEMAND = 'ON_DEMAND'
    SAME_DAY = 'SAME_DAY'
    NEXT_DAY = 'NEXT_DAY'

    ACCEPTED = 'ACCEPTED'
    PICKUP = 'PICKUP'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'
    RETURN = 'RETURNED'

    CASH_ON_PAYMENT = 'CASH'
    ONLINE_PAYMENT = 'ONLINE'

    PRIORITY_CHOICES = (
        (ON_DEMAND, 'ON_DEMAND'),
        (SAME_DAY, 'SAME_DAY'),
        (NEXT_DAY, 'NEXT_DAY')
    )

    STATUS_CHOICES = (
        (ACCEPTED, 'ORDER_ACCEPTED'),
        (PICKUP, 'ORDER_PICKED_UP'),
        (DELIVERED, 'ORDER_DELIVERED'),
        (CANCELLED, 'ORDER_CANCELLED'),
        (RETURN, 'ORDER_RETURNED')
    )

    PAYMENT_TYPE = (
        (CASH_ON_PAYMENT, 'Pay in Cash'),
        (ONLINE_PAYMENT, 'Pay Online')
    )

    title = models.CharField(max_length=100, help_text="product name")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=ON_DEMAND)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACCEPTED)

    weight = models.FloatField(max_length=5, help_text="in kilograms")
    customer_name = models.CharField(max_length=100, null=False, help_text='customer full name')
    customer_contact_no = models.CharField(max_length=15, blank=False, help_text='+8801XXXXXXXXX format preferred')
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    upazila = models.CharField(max_length=20, choices=UPAZILA_CHOICES)
    delivery_location = models.CharField(max_length=100, null=False, help_text='delivery location of the customer')
    delivery_note = models.CharField(max_length=30, null=True, blank=True, help_text='additional notes')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, help_text='price of the product')
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE, default=CASH_ON_PAYMENT)

    created_at = models.DateTimeField(auto_now=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    edited_at = models.DateTimeField(auto_now_add=True)
    celery_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_details', args=[str(self.id)])

    class Meta:
        verbose_name = _("Delivery Task")
        verbose_name_plural = _("Delivery Tasks")
        ordering = ('created_at',)
