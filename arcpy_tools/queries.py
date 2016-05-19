
def queryEquals(field, value, valueIsText):
    """
    Composes the WHERE clause for arcgis definition query.
    Such as "field" = 'value'
    :param field:
    :param value:
    :param valueIsText:
    :return: the query
    """
    if valueIsText:
        return '"{}" = '.format(field) + "'{}'".format(value)
    else:
        return '"{}" = '.format(field) + "{}".format(value)

def queryIN(field, list, valuesAreText):
    """
    Composes the WHERE clause for arcgis definition query.
    Such as "field" IN ('list1', 'list2',...)
    :param field:
    :param list:
    :param valuesAreText:
    """
    q = field + " IN ("

    first = True

    for val in list:
        if not first: q += ", "

        if valuesAreText:
            q += "'{}'".format(val)
        else:
            q += "{}".format(val)

        first = False
    q += ")"

    return q