from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название датчика')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')

    def __str__(self):
        return f'{self.sensor.name}: {self.temperature} °C'
