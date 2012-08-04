from django.contrib.gis.db import models

class Band(models.Model):
    name=models.CharField(max_length=100,unique=True)
    class Meta:
        ordering=ordering=('name',)
    
    def __unicode__(self):
        return u"%s"%(self.name,)

class Album(models.Model):
    band=models.ForeignKey(Band,related_name='albums')
    name=models.CharField(max_length=100)
    cover=models.CharField(max_length=250)
    description=models.TextField()
    class Meta:
        unique_together=(('band','name'),)
    
    def __unicode__(self):
        return u"%s - %s"%(self.name,self.band)
