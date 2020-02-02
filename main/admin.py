from django.contrib import admin
from main.models import Store, Task, DeliveryBoy

# Register your models here.
admin.site.site_header = "GOBD Logistics"
admin.site.site_title = "GOBD Admin Portal"
admin.site.index_title = "Welcome to GOBD Logistics Portal"


# class StoreAdmin(admin.ModelAdmin):
#     list_filter = ['user', 'store_name', 'contact_number', 'nid_number']
#     list_display = ['user', 'store_name', 'contact_number',  'nid_number']
#     search_fields = ['user', 'store_name', 'contact_number', 'nid_number']
#
# class DeliveryBoyAdmin(admin.ModelAdmin):
#     list_filter = ['user', 'name', 'number', 'email', 'nid_number']
#     list_display = ['user', 'name', 'number', 'email', 'nid_number']
#     search_fields = ['user', 'name', 'number', 'email', 'nid_number']

class TaskAdmin(admin.ModelAdmin):
    list_filter = ['title', 'store', 'delivery_boy', 'priority', 'status', 'customer_name', 'customer_contact_no',
                   'delivery_location', 'product_price', 'payment_type']
    list_display = ['title', 'store', 'delivery_boy', 'priority', 'status', 'customer_name', 'customer_contact_no',
                    'delivery_location', 'product_price', 'payment_type']
    search_fields = ['title', 'store', 'delivery_boy', 'priority', 'status', 'customer_name', 'customer_contact_no',
                     'delivery_location', 'product_price', 'payment_type']


# admin.site.register(Store, StoreAdmin)
# admin.site.register(DeliveryBoy, DeliveryBoyAdmin)
admin.site.register(Task, TaskAdmin)

admin.site.register([Store, DeliveryBoy])
