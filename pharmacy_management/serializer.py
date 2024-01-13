from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Customer
        fields='__all__'

class PharmacySerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Pharmacy
        fields='__all__'

class MedicinesSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Medicines
        fields='__all__'

class PurchasingSerializer(serializers.ModelSerializer):
    folder = CustomerSerializer
    folder1 = MedicinesSerializer

    class Meta:
        model=models.Purchasing
        fields='__all__'

class SalesSerializer(serializers.ModelSerializer):
    folder = PharmacySerializer
    folder1 = CustomerSerializer
    folder2 = MedicinesSerializer
    folder3 = PurchasingSerializer

    class Meta:
        model=models.Sales
        fields='__all__'

class ReportsSerializer(serializers.ModelSerializer):
    folder = PurchasingSerializer
    folder1 = SalesSerializer
    folder2 = CustomerSerializer

    class Meta:
        model=models.Reports
        fields='__all__'
