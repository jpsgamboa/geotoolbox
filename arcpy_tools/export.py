
import arcpy

def export_PNG(mxd, outDir, makeDirs=True, resolution = 120, refreshTOC_View = True):
    """
    Refreshes the TOC and the Active View and exports the layout to PDF
    :param mxd:
    :param outpath:
    :param makeDirs:
    :param resolution:
    :param refreshTOC_View:
    """

    import file_system.dir_utils as dh

    if makeDirs:
        dh.create_parent_dir_if_not_exists(outDir)

    if refreshTOC_View:
        arcpy.RefreshTOC()
        arcpy.RefreshActiveView()

    arcpy.mapping.ExportToPNG(mxd, outDir, resolution=resolution)