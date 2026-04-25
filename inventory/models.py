from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    is_open_24h = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.area})"

    class Meta:
        verbose_name_plural = "Pharmacies"
        ordering = ['name']


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    requires_prescription = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class MedicineStock(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='stocks')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine.name} @ {self.pharmacy.name}"

    class Meta:
        unique_together = ('medicine', 'pharmacy')
        ordering = ['medicine__name']
