from django.db import models

class Detalle(models.Model):
    """(Detalle description)"""
    contacto = models.ForeignKey('Contacto')
    telefono = models.CharField('Telefono', max_length=50)
    email = models.EmailField(blank=True)
    facebook = models.CharField(blank=True, max_length=100)
    twitter = models.CharField(blank=True, max_length=100)
    
    def __unicode__(self):
        return u"%s %s" % (self.telefono, self.email)
        

class Contacto(models.Model):
    """(Contacto description)"""
    nombre = models.CharField('Nombre(s)', max_length=100)
    apellido = models.CharField('Apellido(s)', max_length=100)
    
    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.apellido)

