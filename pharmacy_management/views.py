from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializer

@api_view(['GET'])
def customer(request, pk):
    cust = models.Purchasing.objects.filter(cust_ID=pk)
    seria = serializer.PurchasingSerializer(cust, many=True)
    return Response(seria.data)

@api_view(['GET'])
def medicine(request, med):
    med = models.Medicines.objects.filter(name=med)
    seria = serializer.MedicinesSerializer(med, many=True)
    return Response(seria.data)

@api_view(['GET'])
def get_date(request, date_t):
    sold = models.Sales.objects.filter(date=date_t)
    seria = serializer.SalesSerializer(sold, many=True)
    return Response(seria.data)