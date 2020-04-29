# This script is set to be used with Python Window on ArcMap

import arcpy
import os

# To add data to the current MXD (open MXD)
inWorkspace = r"C:\Project" # Set your workspace where your subfolders are kept
mxd = arcpy.mapping.MapDocument("CURRENT")
dataFrame = arcpy.mapping.ListDataFrames(mxd, "*")[0]

walk = arcpy.da.Walk(inWorkspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        layerfile = os.path.join(dirpath, filename)
        addlayer = arcpy.mapping.Layer(layerfile)
        arcpy.mapping.AddLayer(dataFrame, addlayer, "BOTTOM")

arcpy.RefreshTOC()
arcpy.RefreshActiveView()
del addlayer, mxd
