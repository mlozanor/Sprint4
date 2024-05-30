from django.db import models

# Create your models here.
class Solicitud(models.Model):
    id= models.IntegerField(primary_key = True)
    tipo= models.CharField(max_length=50, default= None)
    fecha= models.DateField()   #Fecha de creación 
    
    
    def __str__(self):
        return '%s , %s, %s, %s, %s, %s'%(self.id, self.tipo, self.fecha )