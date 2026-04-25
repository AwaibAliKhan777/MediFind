from rest_framework import serializers
from .models import Medicine, Pharmacy, MedicineStock


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class MedicineStockSerializer(serializers.ModelSerializer):
    pharmacy = PharmacySerializer(read_only=True)
    medicine = MedicineSerializer(read_only=True)

    class Meta:
        model = MedicineStock
        fields = '__all__'


class SearchResultSerializer(serializers.ModelSerializer):
    pharmacy_name = serializers.CharField(source='pharmacy.name')
    pharmacy_area = serializers.CharField(source='pharmacy.area')
    pharmacy_address = serializers.CharField(source='pharmacy.address')
    pharmacy_phone = serializers.CharField(source='pharmacy.phone')
    pharmacy_is_open_24h = serializers.BooleanField(source='pharmacy.is_open_24h')
    medicine_name = serializers.CharField(source='medicine.name')
    medicine_generic = serializers.CharField(source='medicine.generic_name')
    medicine_category = serializers.CharField(source='medicine.category')
    requires_prescription = serializers.BooleanField(source='medicine.requires_prescription')

    class Meta:
        model = MedicineStock
        fields = [
            'id', 'medicine_name', 'medicine_generic', 'medicine_category',
            'requires_prescription', 'pharmacy_name', 'pharmacy_area',
            'pharmacy_address', 'pharmacy_phone', 'pharmacy_is_open_24h',
            'quantity', 'price', 'is_available', 'updated_at'
        ]
