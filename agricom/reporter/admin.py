from django.contrib import admin
from .models import Incidences,Counties
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
	list_display=('name','location')
	default_zoom=8 

class CountiesAdmin(LeafletGeoAdmin):
	list_display=('counties','codes')
	default_zoom=8 
admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
