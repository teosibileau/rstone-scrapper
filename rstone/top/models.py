from django.contrib.gis.db import models
from albums.models import Album
from artists.models import Artist

class Ranking(models.Model):
    title=models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s"%self.title

from polymorphic import PolymorphicModel

class Top(PolymorphicModel):
    ranking=models.ForeignKey(Ranking)
    position=models.PositiveIntegerField()
    site_url=models.URLField(blank=True,null=True)
    class Meta:
        ordering=('position',)

class TopAlbum(Top):
    album=models.ForeignKey(Album,related_name='in_rankings')
    def __unicode__(self):
        return u"%s | %s"%(self.position, self.album)
    

class TopArtist(Top):
    artist=models.ForeignKey(Artist,related_name='in_rankings')
    def __unicode__(self):
        return u"%s | %s"%(self.position, self.artist)
    
    