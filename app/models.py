from django.db import models


# Create your models here.
class DestinatarioEncomienda(models.Model):
    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    fecha = models.DateField()
    Dirección = models.CharField(max_length=60)
    descripción = models.TextField(max_length=300)
    #imagen = models.ImageField(upload_to="Correspondencia, null=True")
    

    def __str__(self):
        return self.nombre 

    