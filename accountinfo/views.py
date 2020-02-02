from django.views import generic
from .models import *
from main.views import *


class UpdateStore(CreateView):
    model = StoreUpdate
    fields = ['store_name', 'seller_name', 'email', 'contact_number',
              'division', 'district', 'upazila', 'business_address', 'nid_number', 'verification']
    template_name = 'information/store_update.html'
    context_object_name = 'update_store'


class EditStore(UpdateView):
    model = StoreUpdate
    fields = ['store_name', 'seller_name', 'email', 'contact_number',
              'division', 'district', 'upazila', 'business_address', 'nid_number', 'verification']
    template_name = 'information/store_details.html'
    context_object_name = 'edit_store'


class StoreInfo(generic.ListView):
    context_object_name = 'store_info'
    template_name = 'information/store_info.html'

    def get_queryset(self):
        return StoreUpdate.objects.all()


class UpdateDeliveryBoy(CreateView):
    model = DeliveryBoyUpdate
    fields = ('name', 'number', 'email', 'division',
              'district', 'upazila', 'address', 'nid_number', 'verification')
    template_name = 'information/delivery_boy_update.html'
    context_object_name = 'update_delivery_boy'


class EditDeliveryBoy(UpdateView):
    model = DeliveryBoyUpdate
    fields = ('name', 'number', 'email', 'division',
              'district', 'upazila', 'address', 'nid_number', 'verification')
    template_name = 'information/delivery_boy_details.html'
    context_object_name = 'edit_delivery_boy'


class DeliveryBoyInfo(generic.ListView):
    context_object_name = 'delivery_boy_info'
    template_name = 'information/delivery_boy_info.html'

    def get_queryset(self):
        return StoreUpdate.objects.all()
