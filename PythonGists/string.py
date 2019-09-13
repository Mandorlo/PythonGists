'''
This module provides a set of useful functions on strings

To transform them in lists :

- `explode_protected` to explode a string in a smart way


'''

def explode_protected(delim, str, protectors = ['()']) -> list:
    """
    like explode function but it will protect delimiters that are protected by protector<br>
    look in test/test_string.py for examples
    
    Warnings
    --------
    This does not check if the protectors are balanced and it only works for delimiters of length 1
    

    Parameters
    ----------
    delim:      str | list
                delimiter string to explode str or a list of delimiters.<br>
                Only delimiters of length 1 are supported
    str:        str
                the string to be exploded
    protectors: list, optional
                list of strings like `['()', '""']`. All strings should be of length 2
                1st char of string is the opening protector, the 2nd if the closing protector
                so all delim characters between the protectors will be ignored during epxlode process

    Returns
    -------
    list
        the list of exploded parts of str
    
    """

    mem = 0
    result = []
    
    # prepare delimiters
    delims = delim if isinstance(delim, list) else [delim]
    for d in delims:
        if len(d) > 1: raise Exception("In explode_protected, all delimiters should be of length 1 !")

    protect_starts = list(map(lambda pr: pr[0], protectors))
    protect_ends = list(map(lambda pr: pr[1], protectors))

    new_str = ''
    for c in str:
        if c in protect_starts:
            new_str += c
            mem += 1
        elif c in protect_ends:
            new_str += c
            mem -= 1
        elif c in delims:
            if mem == 0:
                result.append(new_str.strip())
                new_str = ''
            else:
                new_str += c
        else:
            new_str += c
    
    if new_str != '': result.append(new_str.strip())
    return result
 