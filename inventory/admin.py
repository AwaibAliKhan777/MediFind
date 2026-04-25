from django.contrib import admin
from .models import Medicine, Pharmacy, MedicineStock


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'phone', 'is_open_24h']
    list_filter = ['area', 'is_open_24h']
    search_fields = ['name', 'area', 'address']


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'generic_name', 'category', 'requires_prescription']
    list_filter = ['category', 'requires_prescription']
    search_fields = ['name', 'generic_name', 'category']


@admin.register(MedicineStock)
class MedicineStockAdmin(admin.ModelAdmin):
    list_display = ['medicine', 'pharmacy', 'quantity', 'price', 'is_available', 'updated_at']
    list_filter = ['is_available', 'pharmacy__area']
    search_fields = ['medicine__name', 'pharmacy__name']
    list_editable = ['quantity', 'price', 'is_available']
