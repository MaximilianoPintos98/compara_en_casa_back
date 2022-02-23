from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from app.car.models import Car
from app.car.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['enrollment',]

