'''
This module provides a set of useful functions on dictionaries

For example :

- `get_path` to retrieve a nested element in a dict

'''

def falsy_key(d:dict, key:str) -> bool:
    """
    returns `True` if key is not an attribute of dict `d` or if `d[key]` is falsy

    Returns
    -------
    bool
        False if `d[key]` exists and is not falsy (like `None` or `""`)<br>
        True if `d[key]` does not exist or is falsy

    """
    if not key in d: return True
    if not d[key]: return True
    return False

def get_path(obj, path, delim = '/', return_false_path = False):
    '''
    Returns the value of path in obj
    path is a string of a path delimited by delim

    Parameters
    ----------
    obj:    dict
            a dictionary (if it's sthg else, obj will be returned immediately)
    path:   string
            the path in obj to get what we want
    delim:  str, optional
            the path delimiter (default to "/")
    return_false_path: any, optional
            what to return if the path is not found in obj

    Returns
    -------
    sub_obj: any
        the element in obj at the right path
    return_false_path: any
        if the path is not found in obj
    obj: any
        the original obj if obj is not a dictionary
    '''

    if path == '': return obj
    if not isinstance(obj, dict): return obj
    if path[0] == delim: path = path[1:]
    if path[-1] == delim: path = path[:-1]
    path_list = path.split(delim)

    if len(path_list) == 0 or path == '': return obj

    if path_list[0] in obj: return get_path(obj[path_list[0]], delim.join(path_list[1:]), delim, return_false_path)

    return return_false_path

def dict_inside_out(d) -> dict:
    """
    Turns a dict inside out

    Parameters
    ----------
    d:  dict
        a dictionary to be turned inside out

    Returns
    -------
    dict
        the dict d turned inside out
    """

    newd = {}
    for k, v in d.items():
        if isinstance(v, str):
            newd[v] = k
        elif isinstance(v, list):
            for el in v:
                if isinstance(el, str): newd[el] = k
    return newd
