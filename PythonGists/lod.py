'''
This modules provides useful functions on lists of dicts
'''

import re
from PythonGists.dict import get_path

def lod_find(list_of_dict, key, val, return_val_if_false = False):
    """
    returns the first dict d in list_of_dict where `d[key] = val`
    returns `return_val_if_false` if nothing is found

    Parameters
    ----------
    list_of_dict:   list
                    the source list of dictionaries
    key:            str
                    the dict key
    val:            any
                    the expected value for `d[key]`
    return_val_if_false: any, optional
                    returned if nothing is found
                    default to False

    Returns
    -------
    dict
        the first dict d where d[key] = val if it is found
    return_val_if_false
        if no matching dict is found

    """
    for d in list_of_dict:
        if isinstance(d, dict) and d[key] == val: return d
    return return_val_if_false


def lod_filter(lod, filters = []):
    '''
    Filters elements of a list of dicts (lod)<br>
    e.g. `filters = ['@size/MB > 1000', '@last_modified > "2019-09-13"']`

    Parameters
    ----------
    lod:    list
            a list of dictionaries
    filters: str | list
            the string containing a bool expression, or a list of such strings
            if it's a list, it will be joined with an "AND" operator
    
    Returns
    -------
    list
        a sub list of lod that contains only the elements that match the filters

    Example
    -------
    A filter like `@size/MB > 1000` will filter only elements `d` of `lod` such that `d['size']['MB'] > 1000`
    This is evaluated with the python eval function

    '''
    if isinstance(filters, str): filters = [filters]
    if not isinstance(filters, list) or len(lod) == 0 or len(filters) == 0: return lod

    def prepare_filters(d, filters_s):
        filters_parsed = filters_s
        attributes = list(map(lambda x: x[1], re.findall(r"(^|\s)(\@[^\s]+)(\s|$)", filters_parsed)))
        for attr in attributes:
            v = get_path(d, attr[1:], '/', False)
            if v != False:
                if isinstance(v, str): filters_parsed = filters_parsed.replace(attr, '"' +v + '"')
                elif isinstance(v, float) or isinstance(v, int): filters_parsed = filters_parsed.replace(attr, str(v))
                else: filters_parsed = filters_parsed.replace(attr, str(v))
            else: return "False"
        return filters_parsed

    filters_s = ' and '.join(filters)
    return list(filter(lambda d: eval(prepare_filters(d, filters_s)), lod))
