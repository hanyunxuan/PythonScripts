import arcpy
mxd = arcpy.mapping.MapDocument(r"H:\map2.mxd")
df  = arcpy.mapping.ListDataFrames(mxd)[0]
lyr = arcpy.management.MakeFeatureLayer(r"H:\2.shp").getOutput(0)
arcpy.mapping.AddLayer(df, lyr, "TOP")