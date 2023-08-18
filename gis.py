from cartopy import crs, feature
from __future__ import unicode_literals
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
from cartopy.io import shapereader
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

fig = plt.figure(figsize=(10,5))
axes = fig.add_subplot(111, projection = crs.PlateCarree())
axes.set_extent([-20, 40, 0, 25])

countries = ('Benin','Burkina Faso', 'Cameroon','Chad', 'Niger', 
             'Ivory Coast', 'Equatorial Guinea', 'The Gambia', 'Ghana', 
             'Guinea', 'Guinea-Bissau', 'Liberia', 'Mali', 'Mauritania', 
             'Nigeria', 'Senegal', 'Sierra Leone', 'Togo')
for record, country in zip(shp.records(), shp.geometries()):
    name = record.attributes['ADMIN']
    if name in countries:
        facecolor = 'forestgreen'
        axes.add_geometries([country], crs.PlateCarree(), 
                          edgecolor='black', facecolor = facecolor, alpha = 0.5)
        axes.text(record.attributes['LABEL_X'] - .05, record.attributes['LABEL_Y'] - .15,
                  name, va='center', ha='center', transform=crs.Geodetic(), fontweight='bold',fontsize = '7')
        axes.plot(record.attributes['LABEL_X'],                            
                record.attributes['LABEL_Y']+ 0.5,'ko', ms=3)#, color='k')
