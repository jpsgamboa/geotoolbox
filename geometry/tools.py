
def merge_ogr(output_dir, input_dir_list):
    """
    Merges the files in the provided directory using ogr2ogr
    :param output_dir:
    :param input_dir_list:
    :returns the output dir
    """
    from __tools__.merge import merge_ogr as m
    return m(output_dir, input_dir_list)

def clip_ogr(target_geom_dir, clip_geom_dir, output_dir):
    """
    Clips the target geometry with the provided clip geometry using ogr2ogr
    :param target_geom_dir:
    :param clip_geom_dir:
    :param output_dir:
    :returns the output dir
    """
    from __tools__.clip import clip_ogr as c
    return c(target_geom_dir, clip_geom_dir, output_dir)

def extract_by_query_ogr(input_dir, output_dir, query):
    """
    Generates a new file with the result of the provided query
    :param input_dir:
    :param output_dir:
    :param query:
    :return: the output dir
    """
    from __tools__.extract import extract_by_query_ogr as e
    return e(input_dir, output_dir, query)

def distance_crow_flies(latA, lngA, latB, lngB):
    """
    :param latA:
    :param lngA:
    :param latB:
    :param lngB:
    :return: Returns the linear distance between two coordinates
    """
    from point import Point
    p1 = Point(lngA, latA)
    p2 = Point(lngB, latB)

    return p1.distance_from(p2)
