from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre