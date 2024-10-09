from django.db import models

# Create your models here.
class VENTAS(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID") 
    cantidad = models.IntegerField (verbose_name= "Cantidad",null=False, blank=False)
    precio = models.DecimalField (max_digits= 20, decimal_places=2, verbose_name="Precio", null=False, blank=False)
    vendedor = models.CharField (max_length= 80, verbose_name="Vendedor",null=False, blank=False)
    impuestos = models.DecimalField (max_digits= 20, decimal_places=2, verbose_name="Impuestos", null=False, blank=False)
    comprador = models.CharField(max_length=80, verbose_name="Comprador",null=False, blank=False)
    fecha = models.DateTimeField(verbose_name="Fecha", null=False, blank=False)
    
    