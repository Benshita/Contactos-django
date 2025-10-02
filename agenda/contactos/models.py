from django.db import models

PAISES = [
    ('CL', 'Chile (+56)'),
    ('AR', 'Argentina (+54)'),
    ('PE', 'Perú (+51)'),
    ('BR', 'Brasil (+55)'),
    ('US', 'Estados Unidos (+1)'),
    ('MX', 'México (+52)'),
    ('CO', 'Colombia (+57)'),
    ('ES', 'España (+34)'),
    
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=2, choices=PAISES, default='CL')
    telefono = models.CharField(max_length=13)
    correo = models.EmailField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre