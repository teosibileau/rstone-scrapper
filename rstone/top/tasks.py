from celery.task import task

import logging, os
import logging.handlers

logger = logging.getLogger('rstone')

from albums.models import *
from rstone.top.models import *

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

@task
def addAlbum(a):
    a=Struct(**a)
    try:
        ranking=Ranking.objects.get(title=a.ranking)
        logger.info('%s already exits, getting instance of ranking'%ranking.title)
    except:
        ranking=Ranking(title=a.ranking)
        ranking.save()
        logger.info('No instance of %s exits, generating ranking'%ranking.title)
    try:
        band=Band.objects.get(name=a.artist)
        logger.info('%s already exits, getting instance of band'%band.name)
    except:
        band=Band(name=a.artist)
        band.save()
        logger.info('%s does not exits, generating band'%band.name)
    try:
        album=Album.objects.get(name=a.title,band=band)
        logger.info('%s already exits, getting instance of album'%album.name)
    except:
        album=Album()
        album.name=a.title
        album.band=band
        album.cover=a.cover
        album.description=a.description
        album.save()
        logger.info('%s does not exits, generating instance of band'%album.name)
    try:
        top=TopAlbum.objects.get(ranking=ranking,position=a.position)
        logger.info('album already present in %s at position %s, getting instance'%(ranking.title,a.position))
    except:
        top=TopAlbum()
        top.ranking=ranking
        top.album=album
        top.position=a.position
        top.site_url=a.url
        top.save()
        logger.info('album absent in %s at position %s, creating instance'%(ranking.title,a.position))
    