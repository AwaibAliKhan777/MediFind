import random
from django.core.management.base import BaseCommand
from inventory.models import Medicine, Pharmacy, MedicineStock


class Command(BaseCommand):
    help = 'Seed database with sample data for Bhopal pharmacies'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        pharmacies_data = [
            {'name': 'Apollo Pharmacy', 'area': 'MP Nagar', 'address': 'Zone-1, MP Nagar, Bhopal', 'phone': '9876543210', 'is_open_24h': True},
            {'name': 'MedPlus', 'area': 'Arera Colony', 'address': 'E-5, Arera Colony, Bhopal', 'phone': '9876543211', 'is_open_24h': False},
            {'name': 'Jan Aushadhi Kendra', 'area': 'Habibganj', 'address': 'Near Station, Habibganj, Bhopal', 'phone': '9876543212', 'is_open_24h': False},
            {'name': 'Sharma Medical Store', 'area': 'New Market', 'address': 'Shop 12, New Market, Bhopal', 'phone': '9876543213', 'is_open_24h': False},
            {'name': 'City Care Pharmacy', 'area': 'Kolar Road', 'address': 'Main Road, Kolar, Bhopal', 'phone': '9876543214', 'is_open_24h': True},
            {'name': 'Life Line Medical', 'area': 'Shahpura', 'address': 'Near Lake, Shahpura, Bhopal', 'phone': '9876543215', 'is_open_24h': False},
            {'name': 'Wellness Pharmacy', 'area': 'Govindpura', 'address': 'Industrial Area, Govindpura, Bhopal', 'phone': '9876543216', 'is_open_24h': False},
            {'name': 'Netaji Medical Store', 'area': 'Bairagarh', 'address': 'Main Chowk, Bairagarh, Bhopal', 'phone': '9876543217', 'is_open_24h': False},
        ]

        pharmacies = []
        for p in pharmacies_data:
            obj, _ = Pharmacy.objects.get_or_create(name=p['name'], defaults=p)
            pharmacies.append(obj)

        medicines_data = [
            {'name': 'Paracetamol 500mg', 'generic_name': 'Acetaminophen', 'category': 'Pain Relief', 'manufacturer': 'Cipla', 'requires_prescription': False},
            {'name': 'Azithromycin 500mg', 'generic_name': 'Azithromycin', 'category': 'Antibiotic', 'manufacturer': 'Sun Pharma', 'requires_prescription': True},
            {'name': 'Metformin 500mg', 'generic_name': 'Metformin HCl', 'category': 'Diabetes', 'manufacturer': 'Glenmark', 'requires_prescription': True},
            {'name': 'Omeprazole 20mg', 'generic_name': 'Omeprazole', 'category': 'Antacid', 'manufacturer': 'Dr. Reddys', 'requires_prescription': False},
            {'name': 'Cetirizine 10mg', 'generic_name': 'Cetirizine HCl', 'category': 'Allergy', 'manufacturer': 'Lupin', 'requires_prescription': False},
            {'name': 'Amlodipine 5mg', 'generic_name': 'Amlodipine', 'category': 'Blood Pressure', 'manufacturer': 'Torrent', 'requires_prescription': True},
            {'name': 'Atorvastatin 10mg', 'generic_name': 'Atorvastatin', 'category': 'Cholesterol', 'manufacturer': 'Pfizer', 'requires_prescription': True},
            {'name': 'Dolo 650', 'generic_name': 'Paracetamol 650mg', 'category': 'Pain Relief', 'manufacturer': 'Micro Labs', 'requires_prescription': False},
            {'name': 'Pantoprazole 40mg', 'generic_name': 'Pantoprazole', 'category': 'Antacid', 'manufacturer': 'Alkem', 'requires_prescription': False},
            {'name': 'Amoxicillin 500mg', 'generic_name': 'Amoxicillin', 'category': 'Antibiotic', 'manufacturer': 'Ranbaxy', 'requires_prescription': True},
            {'name': 'Vitamin D3 60000 IU', 'generic_name': 'Cholecalciferol', 'category': 'Vitamins', 'manufacturer': 'Abbott', 'requires_prescription': False},
            {'name': 'Ibuprofen 400mg', 'generic_name': 'Ibuprofen', 'category': 'Pain Relief', 'manufacturer': 'Cipla', 'requires_prescription': False},
        ]

        medicines = []
        for m in medicines_data:
            obj, _ = Medicine.objects.get_or_create(name=m['name'], defaults=m)
            medicines.append(obj)

        for medicine in medicines:
            for pharmacy in pharmacies:
                if random.random() > 0.3:
                    MedicineStock.objects.get_or_create(
                        medicine=medicine,
                        pharmacy=pharmacy,
                        defaults={
                            'quantity': random.randint(0, 100),
                            'price': round(random.uniform(10, 500), 2),
                            'is_available': random.random() > 0.2,
                        }
                    )

        self.stdout.write(self.style.SUCCESS(f'Seeded {len(pharmacies)} pharmacies, {len(medicines)} medicines with stock data!'))
