from django.db import models

class Detalle(models.Model):
    """(Detalle description)"""
    telefono = models.IntegerField('Telefono')
    email = models.EmailField(blank=True)
    facebook = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    
    def __unicode__(self):
        return u"Detalle"
        

class Contacto(models.Model):
    """(Contacto description)"""
    nombre = models.CharField('Nombre(s)', max_length=100)
    apellido1 = models.CharField('Primer Apellido', max_length=100)
    apellido2 = models.CharField('Segundo Apellido', blank=True, max_length=100)
    detalle = models.ForeignKey(Detalle)
    
    def __unicode__(self):
        return self.nombre

