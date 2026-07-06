from rest_framework import viewsets, mixins

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        return SensorSerializer


class MeasurementViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
