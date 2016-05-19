

def merge_ogr(output_dir, input_dir_list):
    from borrowed import ogr2ogr
    ogr2ogr.main(["", output_dir, input_dir_list[0]])

    listIter = iter(input_dir_list)
    next(listIter)

    for path in listIter:
        ogr2ogr.main(["", "-update", "-append", output_dir, path])

    return output_dir
