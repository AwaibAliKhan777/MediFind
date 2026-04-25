from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'medicines', views.MedicineViewSet)
router.register(r'pharmacies', views.PharmacyViewSet)
router.register(r'stocks', views.MedicineStockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.search_medicine, name='search-medicine'),
    path('areas/', views.get_areas, name='get-areas'),
    path('medicines-list/', views.get_medicines_list, name='medicines-list'),
]
