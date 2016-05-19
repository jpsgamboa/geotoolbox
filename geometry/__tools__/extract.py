

def extract_by_query_ogr(input_dir, output_dir, query):
    from borrowed import ogr2ogr
    ogr2ogr.main(["", "-where", query, output_dir, input_dir])
    return output_dir