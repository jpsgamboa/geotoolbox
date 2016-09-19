
import os
from borrowed import ogr2ogr
import file_system.dir_utils as dirutils

def geojson_to_shapefile (inputFile, outputDir, outputName):
    if inputFile.endswith(".geojson"):
        dirutils.create_dir_if_not_exists(outputDir)

        outFull = outputDir + "\\" + outputName + ".shp"

        ogr2ogr.main(["", "-f", "ESRI Shapefile", "-overwrite", outFull, inputFile])
        return outFull
    else:
        return "No GeoJSON found in the provided path."

def geojson_to_shapefile_recursive(inputPath, outputPath):
    dirutils.create_dir_if_not_exists(outputPath)
    dirutils.clear_dir(outputPath)
    #gdal.PushErrorHandler('CPLQuietErrorHandler')
    filesToConvert = os.listdir(inputPath)
    for f in filesToConvert:
        fName = f.split(".")[0]
        geojson_to_shapefile(inputPath + "\\" + f, outputPath, fName)
    print("GeoJSON to Shapefile done")