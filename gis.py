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
axes.set_xticks([-20,-10,0,10,20], crs=crs.PlateCarree())
axes.set_yticks([0,5,10,15,20,25], crs=crs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
axes.xaxis.set_major_formatter(lon_formatter)
axes.yaxis.set_major_formatter(lat_formatter)
ax = axes.inset_axes([0.64,0.5,0.5,0.5],projection = crs.PlateCarree())
ax.set_extent([-20, 55, -32, 35])
ax.add_feature(feature.COASTLINE)
ax.add_feature(feature.BORDERS)
ax.add_feature(feature.STATES, linewidth = 0.2)
# ax.set_xticks([-20,0,20,40], crs=crs.PlateCarree())
# ax.set_yticks([-30,-10,10,30], crs=crs.PlateCarree())
ax.stock_img()
ax.gridlines()
kw = dict(resolution='50m', category='cultural',
          name='admin_0_countries')
states_shp = shapereader.natural_earth(**kw)
shp = shapereader.Reader(states_shp)

for record, country in zip(shp.records(), shp.geometries()):
    name = record.attributes['ADMIN']
    if name in countries:
        ax.add_geometries([country], crs.PlateCarree(), edgecolor='black', facecolor = facecolor)

plt.title('A Map of West Africa')
plt.savefig(west_africa.svg)
