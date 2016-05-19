

def get_extents_of(padding_percent, *layers):
    """
    :param padding_percent: the percentage of the the total extent to apply to the padding (meaning, how far from the
     edges of the data frame should the features be)
    :param layers: the layers to be included in the extent analysis
    :return: the new extent
    """
    finalExtent = layers[0].getExtent(True)

    #Get the minimum and maximum bounds
    for layer in layers:
        extent = layer.getExtent(True)
        if extent.YMin < finalExtent.YMin: finalExtent.YMin = extent.YMin
        if extent.YMax > finalExtent.YMax: finalExtent.YMax = extent.YMax
        if extent.XMin < finalExtent.XMin: finalExtent.XMin = extent.XMin
        if extent.XMax > finalExtent.XMax: finalExtent.XMax = extent.XMax

    dY = (finalExtent.YMax - finalExtent.YMin) * padding_percent/100
    dX = (finalExtent.XMax - finalExtent.XMin) * padding_percent/100

    finalExtent.YMin -= dY
    finalExtent.YMax += dY
    finalExtent.XMin -= dX
    finalExtent.XMax += dX

    return finalExtent
