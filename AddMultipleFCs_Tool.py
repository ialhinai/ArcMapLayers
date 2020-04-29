# This Script is for use within a Tool where users are prompted to select the input folder

import arcpy
import os

# To add data to the current MXD (open MXD)
mxd = arcpy.mapping.MapDocument("CURRENT")
dataFrame = arcpy.mapping.ListDataFrames(mxd, "*")[0]

# To prompt user to select the input folder
inWorkspace = arcpy.GetParameterAsText(0)
walk = arcpy.da.Walk(inWorkspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        layerfile = os.path.join(dirpath, filename)
        addlayer = arcpy.mapping.Layer(layerfile)
        arcpy.mapping.AddLayer(dataFrame, addlayer, "BOTTOM")

arcpy.RefreshTOC()
arcpy.RefreshActiveView()
del addlayer, mxd
