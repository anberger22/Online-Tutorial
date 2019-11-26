import arcpy
arcpy.env.workspace = "D:/Pass/Anika/Other/Tutorials/Data"
feature_list = arcpy.ListFeatureClasses() #to see what data we have, list feature classes
print feature_list
points = "D:/Pass/Anika/Other/Tutorials/Data/ne_10m_populated_places.shp"
countries = "D:/Pass/Anika/Other/Tutorials/Data/ne_10m_admin_0_countries.shp"
outpath = "D:/Pass/Anika/Other/Tutorials/Outputs" #create variable for the path where new files should be saved to

arcpy.MakeFeatureLayer_management(points, "points_layer")
arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "NAME" = 'United States' """)
arcpy.SelectLayerByLocation_management("points_layer", "WITHIN", "countries_layer")
arcpy.FeatureClassToFeatureClass_conversion("points_layer", outpath, "cities_in_us")
