import logging, os
import logging.handlers

logger = logging.getLogger('rstone')

from albums.models import *
from rstone.top.models import *

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

class RankingWrapper:
    def __init__(self,a):
        a=Struct(**a)
        try:
            self.ranking=Ranking.objects.get(title=a.ranking)
            logger.info('%s already exits, getting instance of ranking'%self.ranking.title)
        except:
            self.ranking=Ranking(title=a.ranking)
            self.ranking.save()
            logger.info('No instance of %s exits, generating ranking'%self.ranking.title)
        try:
            self.band=Band.objects.get(name=a.artist)
            logger.info('%s already exits, getting instance of band'%self.band.name)
        except:
            self.band=Band(name=a.artist)
            self.band.save()
            logger.info('%s does not exits, generating band'%self.band.name)
        try:
            self.album=Album.objects.get(name=a.title,band=self.band)
            logger.info('%s already exits, getting instance of album'%self.album.name)
        except:
            self.album=Album()
            self.album.name=a.title
            self.album.band=self.band
            self.album.cover=a.cover
            self.album.description=a.description
            self.album.save()
            logger.info('%s does not exits, generating instance of band'%self.album.name)
        try:
            self.top=TopAlbum.objects.get(ranking=self.ranking,position=a.position)
            logger.info('album already present in %s at position %s, getting instance'%(self.ranking.title,a.position))
        except:
            self.top=TopAlbum()
            self.top.ranking=self.ranking
            self.top.album=self.album
            self.top.position=a.position
            self.top.save()
            logger.info('album absent in %s at position %s, creating instance'%(self.ranking.title,a.position))