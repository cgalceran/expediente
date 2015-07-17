from django.db import models

# Create your models here.

class PermisoExpediente(models.Model):
    usuario = models.ForeignKey('auth.User')
    temas =  models.ManyToManyField('Tema')

    def __unicode__(self):
        return u'%s-%s' % (self.usuario, [tema for tema in self.temas.all()])

class Tema(models.Model):
    name = models.CharField(max_length=255,null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Provincia(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)

class Distribuidora(models.Model):
    provincia =  models.ForeignKey(Provincia)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)

class Expediente(models.Model):
    tema = models.ForeignKey(Tema,null=True)
    distribuidora = models.ForeignKey(Distribuidora)
    name = models.CharField(max_length=20)
    rendicion = models.CharField(max_length=255, null=True)
    total = models.IntegerField(default=0)
    apertura = models.DateField()
    nota = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.distribuidora, self.name, self.rendicion, self.nota)        

class Item(models.Model):
    expediente = models.ForeignKey(Expediente, related_name="items")
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    fecha_envio = models.DateTimeField()
    fecha_recepcion = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
            return u'%s - %s - %s' % (self.expediente, self.destino, self.fecha_recepcion)


    class Meta:
        ordering = ['expediente__distribuidora__provincia', 'expediente', '-fecha_recepcion']

        


