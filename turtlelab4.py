"""
Turtle Lab Module
=================

Provides an interactive problem solving environment based on Python's turtle graphics

AUTHOR

Chaiporn (Art) Jaikaeo
Intelligent Wireless Networking Group (IWING) -- http://iwing.cpe.ku.ac.th
Department of Computer Engineering
Kasetsart University
chaiporn.j@ku.ac.th
"""
import sys
import os
import inspect
import importlib.util
import pathlib
from types import ModuleType
from textwrap import dedent
from math import sin,cos,radians,sqrt
from collections import namedtuple 

# make sure there is no file named 'turtle.py' inside student's working
# directory
# if pathlib.Path("turtle.py").exists():
#    print("ERROR: A file named 'turtle.py' is detected in your working directory.")
#    print("Please remove or rename it; otherwise the task will not work correctly.")
#    sys.exit(1)

# make sure there is no directory named 'turtle' inside student's working
# directory
#if pathlib.Path("turtle").is_dir():
#    print("ERROR: A directory named 'turtle' is detected in your working directory.")
#    print("Please remove or rename it; otherwise the task will not work correctly.")
#    sys.exit(1)

try:
    INTERACTIVE = (os.environ['ELAB_GRADING'] != '1')
except KeyError:
    INTERACTIVE = True

if INTERACTIVE:
    try:
        # remove the current path out of sys.path to prevent a local turtle.py
        # module to be accidentally imported
        syspath = sys.path
        sys.path = sys.path[1:]

        # make sure 'turtle' module exists before loading
        turtle_spec = importlib.util.find_spec("turtle")
        if turtle_spec is None:
            print(f"ERROR: Standard 'turtle' module not found")
            sys.exit(1)

        try:
            import turtle as std_turtle
        except ImportError as e:
            std_turtle = None
        sys.path = syspath
        
        # make sure 'std_turtle' is indeed the genuine Turtle library
        # (now just check whether there is a Canvas class inside the tkinter
        # module)
        if std_turtle is None or \
           not 'Canvas' in std_turtle.__dict__ or \
           not inspect.isclass(std_turtle.Canvas) or \
           not std_turtle.Canvas.__module__ == 'tkinter':
            print(f"ERROR: Invalid turtle module is found in {turtle_spec.origin}")
            print("Please remove it and rerun the script.")
            sys.exit(1)

        import base64
        from io import BytesIO
        INTERACTIVE = True
        SCREEN_SIZE_X = 1200
        SCREEN_SIZE_Y = 1200
    except ModuleNotFoundError:
        INTERACTIVE = False
        std_turtle = None
    try:
        from PIL import Image,ImageTk
    except ModuleNotFoundError:
        Image = None
        ImageTk = None


#############################
class array(list):
    def __init__(self,elements):
        list.__init__(self,elements)

    def __add__(self,value):
        if isinstance(value,array):
            return array([x+y for x,y in zip(self,value)])
        if isinstance(value,(int,float)):
            return array([x+value for x in self])

    def __radd__(self,value):
... (605 lines left)