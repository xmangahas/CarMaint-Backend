from django.shortcuts import render, redirect

from .models import Car, Maintenance

from .forms import CarForm, MaintenanceForm

# Create your views here.

def car_list(request):
    cars = Car.objects.all()
    return render(request, "carmaint/car_list.html", {"cars": cars})

def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    return render(request, "carmaint/maintenance_list.html", {"maintenances": maintenances})

def car_detail(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'carmaint/car_detail.html', {'car': car})

def maintenance_detail(request, pk):
    maintenance = Maintenance.objects.get(id=pk)
    return render(request, 'carmaint/maintenance_detail.html', {'maintenance': maintenance})

def car_create(request):
    if request.method == 'POST':
        #add new car to database
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        # if it's a get request, render form
        form = CarForm()
    return render(request, 'carmaint/car_form.html', {'form': form})

def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'carmaint/car_form.html', {'form': form})

def car_delete(request, pk):
    #car = Car.objects.get(pk=pk)
    Car.objects.get(id=pk).delete()
    return redirect('car_list')

def maintenance_create(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save()
            return redirect('car_detail', pk=maintenance.car.pk)
    else:
        form = MaintenanceForm()
    return render(request, 'carmaint/maintenance_form.html', {'form': form})

def maintenance_edit(request, pk):
    maintenance = Maintenance.objects.get(pk=pk)
    if request.method == "POST":
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            maintenance = form.save()
            return redirect('car_detail', pk=maintenance.car.pk)
    else:
        form = MaintenanceForm(instance=maintenance)
    return render(request, 'carmaint/maintenance_form.html', {'form': form})

def maintenance_delete(request, pk):
    maintenance = Maintenance.objects.get(pk=pk)
    Maintenance.objects.get(id=pk).delete()
    return redirect('car_detail', pk=maintenance.car.pk)

# from rest_framework import generics
# from .serializers import CarSerializer, MaintenanceSerializer
# from .models import Car, Maintenance
# from datetime import date

# class CarList(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CarDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class MaintenanceList(generics.ListCreateAPIView):
#     queryset = Maintenance.objects.all()
#     serializer_class = MaintenanceSerializer

# class MaintenanceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Maintenance.objects.all()
#     serializer_class = MaintenanceSerializer
