import arcpy
arcpy.env.workspace = "D:/Pass/Anika/Other/Tutorials/Data"
arcpy.env.overwriteOutput = True

feature_list = arcpy.ListFeatureClasses() #to see what data we have, list feature classes
print feature_list
points = "D:/Pass/Anika/Other/Tutorials/Data/ne_10m_populated_places.shp"
countries = "D:/Pass/Anika/Other/Tutorials/Data/ne_10m_admin_0_countries.shp"
outpath = "D:/Pass/Anika/Other/Tutorials/Outputs" #create variable for the path where new files should be saved to

countries_of_interest = ["United States of America", "Italy", "Kenya", "Jordan", "Lebanon", "Scotland", "France"]

arcpy.MakeFeatureLayer_management(points, "points_layer")

for x in countries_of_interest:
    print x
    arcpy.MakeFeatureLayer_management(countries, "countries_layer", """ "NAME" = '{}' """.format(x)) #adding .format(x) at the end of the string allows it to substitute whatever is in the {} with the name of x in the list 
    arcpy.SelectLayerByLocation_management("points_layer", "WITHIN", "countries_layer")
    arcpy.FeatureClassToFeatureClass_conversion("points_layer", outpath, "cities_in_{}".format(x))
