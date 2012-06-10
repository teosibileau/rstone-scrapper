from django.contrib.gis.db import models
from albums.models import Album

class Ranking(models.Model):
    title=models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s"%self.title
    
class TopAlbum(models.Model):
    ranking=models.ForeignKey(Ranking,related_name='albums')
    album=models.ForeignKey(Album,related_name='in_rankings')
    position=models.PositiveIntegerField()
    class Meta:
        ordering=('position',)
        unique_together=(('ranking','album'),)
    def __unicode__(self):
        return u"%s | %s"%(self.position, self.album)
    
