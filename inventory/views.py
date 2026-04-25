from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Medicine, Pharmacy, MedicineStock
from .serializers import (
    MedicineSerializer, PharmacySerializer,
    MedicineStockSerializer, SearchResultSerializer
)


@api_view(['GET'])
def search_medicine(request):
    query = request.GET.get('q', '').strip()
    area = request.GET.get('area', '').strip()
    available_only = request.GET.get('available', 'false').lower() == 'true'

    if not query:
        return Response({'error': 'Search query required'}, status=status.HTTP_400_BAD_REQUEST)

    stocks = MedicineStock.objects.select_related('medicine', 'pharmacy').filter(
        Q(medicine__name__icontains=query) |
        Q(medicine__generic_name__icontains=query) |
        Q(medicine__category__icontains=query)
    )

    if area:
        stocks = stocks.filter(pharmacy__area__icontains=area)

    if available_only:
        stocks = stocks.filter(is_available=True, quantity__gt=0)

    serializer = SearchResultSerializer(stocks, many=True)
    return Response({
        'query': query,
        'count': stocks.count(),
        'results': serializer.data
    })


@api_view(['GET'])
def get_areas(request):
    areas = Pharmacy.objects.values_list('area', flat=True).distinct().order_by('area')
    return Response(list(areas))


@api_view(['GET'])
def get_medicines_list(request):
    medicines = Medicine.objects.all().order_by('name')
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class MedicineStockViewSet(viewsets.ModelViewSet):
    queryset = MedicineStock.objects.select_related('medicine', 'pharmacy').all()
    serializer_class = MedicineStockSerializer
