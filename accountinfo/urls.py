from django.conf.urls import url
from . import views
from .views import *

# setting the url patterns

urlpatterns = [

    url(r'store/$', views.UpdateStore.as_view(), name="update_store"),
    url(r'store/<int:user_id>/$', views.EditStore, name="edit_store"),
    url(r'store/info/$', views.StoreInfo.as_view(), name='store_info'),

    url(r'deliver/$', views.UpdateDeliveryBoy.as_view(), name="update_delivery_boy"),
    url(r'deliver/<int:user_id>/$', views.EditDeliveryBoy, name="edit_delivery_boy"),
    url(r'deliver/list/$', views.DeliveryBoyInfo, name="delivery_boy_info"),

]