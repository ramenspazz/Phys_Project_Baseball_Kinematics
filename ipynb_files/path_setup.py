import os
import sys
def path_setup():
    #import external modules
    nb_dir = os.path.split(os.getcwd())[0]
    abs_nb_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    module_dir = abs_nb_dir + '/Py_files'
    if module_dir not in sys.path:
        sys.path.append(module_dir)
    return abs_nb_dir