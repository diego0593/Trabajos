from django.db import models

# Create your models here.


class Publicidad(models.Model):
    idAd = models.DecimalField(primary_key=True,max_digits=30,decimal_places=0)
    timestamp = models.TextField(null=True,help_text='Cuando tuvo lugar la impresión')
    domain = models.TextField(null=True,help_text='Dominio en el que se ha mostrado el anuncio')
    language = models.TextField(null=True,help_text='Idioma del browser del usuario')
    userAgent = models.TextField(null=True,help_text='Identificador del browser del usuario')
    publicIP = models.TextField(null=True,help_text='IP del usuario')

    def __str__(self):
        return '{}'.format(self.idAd)

    class Meta:
        verbose_name_plural = 'Publicidad'


class Clicks(models.Model):
    idAd = models.ForeignKey(Publicidad,on_delete=models.CASCADE)
    timestamp = models.TextField(null=True,help_text='Cuando tuvo lugar la impresión')
    clickTime=models.BigIntegerField(null=True, help_text='Tiempo transcurrido hasta que se hizo click (en ms)')

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Clicks'



class Viewability(models.Model):
    idAd = models.ForeignKey(Publicidad,on_delete=models.CASCADE)
    timestamp = models.TextField(null=True,help_text='Cuando tuvo lugar la impresión')
    viewable=models.DecimalField(null=True,max_digits=4,decimal_places=3,help_text='Porcentaje del anuncio visible')

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Viewability'

