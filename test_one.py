from PythonGists.file import import_dir

modules = import_dir('./PythonGists', module_prefix="PythonGists")

res1 = modules['string'].explode_protected(",", "a, bcd, e, (f, g), h", ['()'])

print('ok')