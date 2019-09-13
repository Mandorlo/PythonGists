'''
This module provides functions to manipulate dictionaries and lists (=trees)<br>

## Vocabulary

* A __tree__ in this module means either a list or a dict
* A __leaf__ in this module means the deepest element in a tree that is not a list nor a dict

'''

def is_tree(o) -> bool:
    '''
    tells if o is either :
    
    - a list or dict (true) 
    - or sthg else (false)

    Returns
    -------
    bool
        True if o is either a dict or a list

    '''
    return isinstance(o, list) or isinstance(o, dict)

def tree_simplify(tree):
    '''
    "Simplifies" a tree recursively : if dict or list has only one value, it returns the value

    Returns
    -------
    tree: list | dict
    
    Examples
    --------
    
    - [3] => 3
    - [2, {a: 5}] => [2, 5]
    - [{a: {b: 3}}, {c: 2}, [1, 2], [5]] => [3, 2, [1, 2], 5]

    '''

    if not is_tree(tree): return tree
    if len(tree) == 1: 
        if isinstance(tree, list): return tree_simplify(tree[0])
        if isinstance(tree, dict): return tree_simplify(list(tree.values())[0])

    if isinstance(tree, list): return [tree_simplify(el) if is_tree(el) else el for el in tree]
        
    d = {}
    for k, v in tree.items():
        d[k] = tree_simplify(v) if is_tree(v) else v
    return d


    