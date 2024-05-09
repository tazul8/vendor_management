from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer


class AddVendorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vendor has been added successfully."})
        return Response({"message": "Vendor has not been created. Something is wrong. Try again later."})

        
class VendorListView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all().order_by('-id')
        vendor_serializer = VendorSerializer(vendors, many=True)
        return Response(vendor_serializer.data)
    

class VendorView(APIView):
    def get(self, request, *args, **kwargs):
        vendor_code = request.data.get('vendor_code', None)
        if vendor_code is None:
            return Response({"message": "Vendor code is required."})

        vendor = Vendor.objects.filter(vendor_code=vendor_code).first()
        vendor_serializer = VendorSerializer(vendor)
        return Response(vendor_serializer.data)
    
    def put(self, request, *args, **kwargs):
        vendor_code = request.data.get('vendor_code', None)
        if vendor_code is None:
            return Response({"message": "Vendor code is required."})

        vendor = Vendor.objects.filter(vendor_code=vendor_code).first()
        if len(vendor) > 0:
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"message": "Invalid data"})
        return Response({"message": "No vendor found."})
    
    def delete(self, request, *args, **kwargs):
        vendor_code = request.data.get('vendor_code', None)
        if vendor_code is None:
            return Response({"message": "Vendor code is required."})

        vendor = Vendor.objects.filter(vendor_code=vendor_code).first()
        if len(vendor) > 0:
            vendor.delete()
            return Response({"message": "Vendor has been deleted."})
        else:
            return Response({"message": "No vendor found."})


class AddPurchaseOrderView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Purchase Order has been submitted successfully."})
        return Response({"message": "Something is wrong. Try again later."})

        
class PurchaseOrderListView(APIView):
    def get(self, request):
        objs = PurchaseOrder.objects.all().order_by('-id')
        serializer = PurchaseOrderSerializer(objs, many=True)
        return Response(serializer.data)
    

class PurchaseOrderView(APIView):
    def get(self, request, *args, **kwargs):
        po_number = request.data.get('po_number', None)
        if po_number is None:
            return Response({"message": "PO number is required."})

        obj = PurchaseOrder.objects.filter(po_number=po_number).first()
        obj_serializer = PurchaseOrderSerializer(obj)
        return Response(obj_serializer.data)
    
    def put(self, request, *args, **kwargs):
        po_number = request.data.get('po_number', None)
        if po_number is None:
            return Response({"message": "PO number is required."})

        obj = PurchaseOrder.objects.filter(po_number=po_number).first()
        if len(obj) > 0:
            serializer = PurchaseOrderSerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"message": "Invalid data"})
        return Response({"message": "No order found."})
    
    def delete(self, request, *args, **kwargs):
        po_number = request.data.get('po_number', None)
        if po_number is None:
            return Response({"message": "PO number is required."})

        obj = PurchaseOrder.objects.filter(po_number=po_number).first()
        if len(obj) > 0:
            obj.delete()
            return Response({"message": "Order has been deleted."})
        else:
            return Response({"message": "No order found."})
