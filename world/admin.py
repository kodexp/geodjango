#from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from models import WorldBorder

admin.site.register(WorldBorder, admin.GeoModelAdmin)

# https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/#introduction
#admin.site.register(WorldBorder, admin.OSMGeoAdmin)


