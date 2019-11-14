from rest_framework import serializers
from .models import Car, Maintenance

class CarSerializer(serializers.HyperlinkedModelSerializer):
    maintenances = serializers.HyperlinkedRelatedField(
        view_name='maintenance_detail',
        many=True,
        read_only=True
    )

    car_url = serializers.ModelSerializer.serializer_url_field(
        view_name='car_detail'
    )

    class Meta:
        model = Car
        #fields = ('id', 'photo_url', 'nationality', 'name', 'songs',)
        fields = ('id', 'car_url', 'year', 'make', 'model', 'trim', 'image_url', 'maintenances',)

class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):
    car = serializers.HyperlinkedRelatedField(
        view_name='car_detail',
        read_only=True
    )

    maintenance_url = serializers.ModelSerializer.serializer_url_field(
        view_name='maintenance_detail'
    )

    class Meta:
        model = Maintenance
        fields = ('id', 'maintenance_url', 'desc', 'total_cost', 'mileage', 'notes', 'invoice_img', 'car',)