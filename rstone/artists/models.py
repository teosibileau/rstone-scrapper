from django.db import models
from django.utils.translation import ugettext as _ 

from model_utils import Choices

# Create your models here.
class Artist(models.Model):
    ROLES=Choices(
        ('singer',_('Singer')),
        ('guitarrist',_('Guitarrist'))
    )
    name=models.CharField(max_length=100,unique=True)
    role=models.CharField(max_length=20,choices=ROLES)
    class Meta:
        ordering=('name',)
    
    def __unicode__(self):
        return u"%s"%self.name
    
