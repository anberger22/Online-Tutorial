import arcpy
arcpy.env.workspace = "D:/Pass/Anika/Other/Final_Project/Data"

feature_classes = arcpy.ListFeatureClasses()

for fc in feature_classes:
    spatial_ref = arcpy.Describe(fc).spatialReference
    if spatial_ref.name == "Unknown":
        print("{0} has an unknown spatial reference".format(fc))
    else:
        print("{0}: {1}, {2}".format(fc, spatial_ref.type, spatial_ref.name))
