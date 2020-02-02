from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from main.bd_divisions import DIVISION_CHOICES, DISTRICT_CHOICES, UPAZILA_CHOICES

class StoreUpdate(models.Model):
    update_time = models.DateTimeField(auto_now_add=True)
    user_id = models.AutoField(primary_key=True)
    update_by = models.OneToOneField(User, on_delete=models.CASCADE)

    store_name = models.CharField(max_length=150, null=False, blank=False)
    seller_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=25, null= False, blank=False)
    contact_number = models.CharField(max_length=15, null=False, blank=False)
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    upazila = models.CharField(max_length=20, choices=UPAZILA_CHOICES)
    business_address = models.CharField(max_length=50)
    nid_number = models.CharField(max_length=20)
    verification = models.FileField(upload_to='disk/seller/%Y/%m/%d/')

    def __str__(self):
        return self.store_name

    def get_absolute_url(self):
        return reverse('update_store', args=[str(self.id)])

class DeliveryBoyUpdate(models.Model):
    update_time = models.DateTimeField(auto_now_add=True)
    user_id = models.AutoField(primary_key=True)
    update_by = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, null=False, blank=False)
    number = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    upazila = models.CharField(max_length=20, choices=UPAZILA_CHOICES)
    address = models.CharField(max_length=50, null=True, blank=True)
    nid_number = models.CharField(max_length=20, null=True, blank=True)
    verification = models.FileField(upload_to='disk/delivery_man/%Y/%m/%d/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('update_delivery_boy', args=[str(self.id)])
