#See https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/#introduction

#from django.contrib import admin

from django.contrib.gis import admin
from models import WorldBorder

# Register your models here.
#admin.site.register(WorldBorder, admin.GeoModelAdmin)
# OR
admin.site.register(WorldBorder, admin.OSMGeoAdmin)


