# 💊 MediFind — Medicine Availability Finder

A Django + REST API web app that lets users search for medicine availability across pharmacies in Bhopal.

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install django djangorestframework django-cors-headers
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. Seed sample data (8 Bhopal pharmacies + 12 medicines)
```bash
python manage.py seed_data
```

### 4. Create admin user
```bash
python manage.py createsuperuser
```

### 5. Start the server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/search/?q=paracetamol` | Search medicine |
| GET | `/api/search/?q=dolo&area=MP Nagar` | Filter by area |
| GET | `/api/search/?q=dolo&available=true` | In-stock only |
| GET | `/api/areas/` | List all areas |
| GET | `/api/medicines/` | All medicines (CRUD) |
| GET | `/api/pharmacies/` | All pharmacies (CRUD) |
| GET | `/api/stocks/` | All stock records (CRUD) |
| ANY | `/admin/` | Django Admin panel |

---

## 🗂️ Project Structure
```
medifind/
├── inventory/
│   ├── models.py          # Medicine, Pharmacy, MedicineStock
│   ├── views.py           # Search API + ViewSets
│   ├── serializers.py     # DRF serializers
│   ├── admin.py           # Admin config
│   └── management/
│       └── commands/
│           └── seed_data.py   # Sample data
├── medifind/
│   ├── settings.py
│   └── urls.py
└── templates/
    └── index.html         # Frontend UI
```

---

## 🛣️ Upgrade Roadmap

- [ ] Google Maps API — show pharmacies on map
- [ ] WhatsApp/SMS alerts when medicine restocked
- [ ] Pharmacy owner login to update stock live
- [ ] Mobile app (React Native)
- [ ] OCR prescription scanner

---

## 🔐 Admin
URL: http://127.0.0.1:8000/admin/

