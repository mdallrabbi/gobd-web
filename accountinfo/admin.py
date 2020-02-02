from django.contrib import admin
from accountinfo.models import StoreUpdate, DeliveryBoyUpdate
# Register your models here.
admin.site.site_header = "GOBD Logistics"
admin.site.site_title = "GOBD Admin Portal"
admin.site.index_title = "Welcome to GOBD Logistics Portal"

admin.site.register([StoreUpdate, DeliveryBoyUpdate])
