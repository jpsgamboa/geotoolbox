

def clip_ogr(target_geom_dir, clip_geom_dir, output_dir):
    from borrowed import ogr2ogr
    ogr2ogr.main(["", "-clipsrc", clip_geom_dir, output_dir, target_geom_dir])
    return output_dir