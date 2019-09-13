'''
This module provides useful functions on files

- `search_files` to look for files in a dir
- `load_json_file` to import a json file in a dict/list
- `import_dir` to import python files dynamically

'''

import os, importlib, re, json
from importlib import util

def search_files(dir_path:str, regex = '') -> list:
    '''
    Searches for files in dir_path recursively (uses [os.walk](https://www.geeksforgeeks.org/os-walk-python/)) that match regex (if specified)

    Parameters
    ----------
    dir_path:   str
                the path to the target root dir
    regex:      regex obj, optional
                a regex to filter only some files

    Returns
    -------
    list
        list of absolute file paths
    '''

    myfiles = []

    for r, d, files in os.walk(dir_path): # root, dirs, files
        for file in files:
            if regex == '' or regex == None or re.search(regex, file): myfiles.append(os.path.join(r, file))

    return myfiles

def load_json_file(file_path):
    """
    loads a json file

    .. todo::
        raise error (or return None) if cannot read file or file does not exist or json parse fails

    Parameters
    ----------
    file_path:  str
                the path to the json file

    Returns
    -------
    obj
        return json.load(file) see https://docs.python.org/fr/3/library/json.html#json.load
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    return None



def import_dir(dir_path, regex = None, module_prefix = ""):
    '''
    Imports all modules in dir_path and return them in a dictionary
    
    .. todo::
        add directory recursivity with a 3rd optional "opt" argument

    Parameters
    ----------
    dir_path:   str 
                path of the target directory
    regex:      str, optional
                regex applied to all file names (not paths) to filter results
                default to None

    Returns
    -------
    dict
        keys are file names (without the .py) 
        values are the module objects

    '''
    dict_modules = {}
    if len(module_prefix) > 1 and module_prefix[-1] != '.': module_prefix += "."

    for module in os.listdir(dir_path):
        if module == '__init__.py' or module[-3:] != '.py' or (regex != None and re.search(regex, module) == None): continue
        module_name = module[:-3]
        if not util.find_spec(module_prefix + module_name):
            dict_modules[module_name] = "ERROR"
        else:
            mod = importlib.import_module(module_prefix + module_name)
            dict_modules[module_name] = mod
            
    return dict_modules