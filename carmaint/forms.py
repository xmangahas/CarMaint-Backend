from django import forms
from .models import Car, Maintenance

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('year', 'make', 'model', 'trim', 'image_url')

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ('desc', 'date', 'total_cost', 'mileage', 'notes', 'invoice_img', 'car')