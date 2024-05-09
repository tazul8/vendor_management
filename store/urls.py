from django.urls import path
from .views import *


urlpatterns = [
    path('vendors/', AddVendorView.as_view()),
    path('vendors_list/', VendorListView.as_view()),
    path('vendor/', VendorView.as_view()),
    path('purchase_orders/', AddPurchaseOrderView.as_view()),
    path('purchase_order_list/', PurchaseOrderListView.as_view()),
    path('purchase_order/', PurchaseOrderView.as_view()),
]
