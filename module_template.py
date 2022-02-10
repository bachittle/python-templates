"""module_template

This file has no functionality. It's purpose is to document 
the python document structure that will achieve the best results. 
Following pep convention, it serves as a guide and is not forced upon. 

If you would like to see detailed examples of python modules, go to the 
examples folder. It contains trivial examples such as hello_world.py as well as
real-world examples that I will most likely copy and use in the future,
such as initial setups for tools such as BeautifulSoup, Flask, etc. 

If you have any examples that would be worth adding, read the contributing section to
see how to contribute to this repository. 
"""

"""Import statements

Most of the time, these appear at the top of your python program. 
You can use libraries that you import
"""
#import time

"""function definitions

you can technically write python without ever using functions,
however it is better to modularize your code and functions are
the best way to do it in python (I personally dislike python classes)
"""

# def hello(x):
#   print("Hello", x)  

"""main function

Rather than forcing a main function, python lets you run things globally.

ex: you can do assignment statements without having to be inside a function
x = y + z

This may be ok for scripting, but it's bad when the file is a module. 
If you want to have something run only when called via `python file.py`
and not via importing like `import file`, use this.
"""

# if __name__ == "__main__":
#   print(hello("world"))