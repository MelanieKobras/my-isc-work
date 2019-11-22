"""
map_data.py
===========

Extracts some mapped data from a local file ready for plotting.

"""

from netCDF4 import Dataset
import numpy as np

# Open netCDF dataset and extract data
dataset = Dataset(u"/home/user01/my-isc-work/course_materials/exercises/example_data/tas.nc")
tas = dataset.variables['tas'][0,:].squeeze()
lon_values = dataset.variables['lon'][:]
lat_values = dataset.variables['lat'][:]

# Create meshgrid 
lons, lats = np.meshgrid(lon_values, lat_values)
