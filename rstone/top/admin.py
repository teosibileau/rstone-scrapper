from django.contrib.gis import admin

from rstone.top.models import *

class TopAlbumAdmin(admin.ModelAdmin):
	list_display=('ranking','position','title','band')
	search_fields=('album__name','album__band__name')
	list_filter=('ranking',)
	def title(self,obj):
		return obj.album.name
	
	def band(self,obj):
		return obj.album.band

admin.site.register(Ranking)
admin.site.register(TopAlbum,TopAlbumAdmin)