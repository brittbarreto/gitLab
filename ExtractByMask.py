'''
Created on Jul 6, 2016
Crops a s5t5 to waterways
@author: cade
'''
import arcpy
import glob
import os

from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')

env.workspace = "D:/proj/spot5take5/Raster/Products/Crop_stack"
outws_34 = "D:/proj/spot5take5/Raster/Products/Crop_to_waterways2"
mask = "D:/proj/spot5take5/GIS/delta_merge_fillin.shp"


rasterList_34 = arcpy.ListDatasets("*","Raster")
for i in rasterList_34:
    outExtractByMask = ExtractByMask(i, mask)
    outname = os.path.join(outws_34,str(i))
    print(outname)
    outExtractByMask.save(outname)

daniel = "I like chips"    
    
