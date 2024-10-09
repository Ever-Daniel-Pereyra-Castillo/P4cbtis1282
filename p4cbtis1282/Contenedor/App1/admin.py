from django.contrib import admin
from .models import VENTAS
# Register your models here.

class VentasAdmin(admin.ModelAdmin):
    fields = ["id","cantidad","precio","vendedor","impuestos","comprador","fecha"]
    list_display =["cantidad","fecha"]
    
admin.site.register(VENTAS, VentasAdmin)
