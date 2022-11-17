from django.contrib import admin

from .models import Propietarios,Vehiculos, Marca ,Modelo

# Register your models here.
admin.site.register(Propietarios)
admin.site.register(Vehiculos)
admin.site.register(Marca)
admin.site.register(Modelo)