# ----------------------
# Usage of this program:
# ----------------------
# Delete the examples, and replace with the code you need. 
# This template is essentially how every python program is structured, maybe bits and pieces are swapped
# but this is best practice. Any piece can be omitted, 
# just please delete the sleep functions so your code isn't slow! 


# -------
# Imports
# -------
# Put your import at the beginning of your python program.
# Any libraries you installed with pip can be imported here. 
# You can also import your own code if it is properly structured as modules. 
# If you need a good tutorial, this one seems adequate: 
# https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
# 
# ex:
import time

# ---------------------------
# Accessing imports globally
# ---------------------------
# You can access the imports as variables of the same name. 
# With this example, time is accessed and printed, most likely as module information. 
#
# ex:
print(time)

# Time happens to be an object that has the method sleep. 
# You can call methods globally, and it will run on call/import
# 
# ex:
time.sleep(10) # sleeps for 10 seconds


# ----------------
# Global Variables
# ----------------
# Declaring variables that not wrapped by def: or class: are global variables
# They can be accessed by any succeeding defs or classes. 
# They can also be accessed as an export to other programs. To "hide" as an export, 
# start the variable name with an underscore (ex: _counter = 0).
# 
# ex:
x = 5
y = 10
z = x+y

# --------------------
# Function definitions
# --------------------
# Make your own functions. These can be accessed when imported.  
#
# ex: 
def hello():
  return "Hello! " + z
#
# if I wanted to import this I will do this in another python file:
# 
# import module_template
# print(module_template.hello())
# 


# --------------
# Main functions
# --------------
# If you are familiar with C, you know that there is an int main function that has to be in every C program.
# Python does not require this, however it is good practice to do separate things for main. 
# To do this, use the following template:
#
# this will be called when running the program in python: python module_template.py
# it will NOT be called when importing: import module_template
# everything else will run when importing except for that if statement. 
#

if __name__ == "__main__":
   print(hello()) 
    # replace hello() with what you would like to run in main. 

