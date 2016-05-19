
def generate_GCS_WGS84_prj(outputPath, outputName):
    """
    Generates a .prj file for a shapefile with the WGS84 GCS projection definition
    :param outputPath:
    :param outputName:
    """
    prj = open("%s.prj" % (outputPath + '\\' + outputName), "w")
    prjString = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
    prj.write(prjString)
    prj.close()