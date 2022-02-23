from django.db import models


class Car(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nombre')
  enrollment = models.CharField(max_length=8, blank=True, null=True, verbose_name='Matricula')
  brand = models.CharField(max_length=100, blank=True, null=True, verbose_name='Marca')
  model = models.IntegerField(default=0000, blank=True, null=True, verbose_name='Modelo')
  color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Color')
  owner = models.CharField(max_length=100, blank=True, null=True, verbose_name='Titular Vehiculo')

  class Meta:
    verbose_name = 'Automovil'
    verbose_name_plural = 'Automoviles'
    ordering = ['id']