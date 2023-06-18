'''
Modules and Packages
What is module?
A module is python program, which is saved with extension .py
A module is collection of,
    1. Variables/Objects
    2. Functions
    3. Classes
Python modules are two types
    1. Predefined modules
    2. User defined modules

predefined Modules:
    The existing modules are called predefined modules
    Eg: os,datetime,built-ins,sys,…
    
User defined modules:
    The modules which are developed by programmer are called user defined modules.
    
                                    Bank Applications
    Accounts.py                     Transcation.py              reports.py()
    1) def create_acc():            def deposit():              def passbook():
    2) def update_acc():            def withdraw():             def monthy_report():
    3) def delete_acc():            def tranfser():             def yearly_report():

User defined modules two types
    1. Reusable modules
    2. Executable modules
    
Executable modules: Modules which consists of executable statements 
Reusable modules: This module does not have any executable statements is called reusable module. 
This module is having function definitions and class definitions.
This module can be used in one program/module or more than one program/module.

'''
# # Executable statements:
# def fun1():
#     print("inside the fun1")

# def fun2():
#     print("inside the fun2")

# fun1()
# fun2()
# print("hello")

'''
import statement:
one module import another module using “import” keyword. Using the content of one module inside another module.
Syntax:
    Syntax1: import <module-name>
    Syntax2: import <module-name> as <alias-name>
    Syntax3: from <module-name> import <identifier>,..
    Syntax4: from <module-name> import *
    Syntax5: from <module-name> import <identifier> as <alias-name>

Syntax-1: import <module-name>
    This syntax import the entire module
    Import statement creates name space with module-name and load all the content. 
    
'''
# import module2
# import module1
# module1.fun1()
# module2.fun1()
# module1.fun2() 
# module2.fun2()
# module1.fun3()
# module2.fun3()


'''
Syntax2: import <module-name> as <alias-name>
This syntax import entire module
This syntax import the module with another name/alias name

'''

# import module1 as m1
# import module2 as m2

# m1.fun1()
# m1.fun2()
# m1.fun3()
# m2.fun1()
# m2.fun2()
# m2.fun3()

'''
if we don't want to import entire module then  go for syntax 3
Syntax3 &4 : from <module-name> import <identifier>,..
This syntax import the given identifiers (function-name, object name, class
name) as part of current module

'''

import modulefinder
from module1 import fun1, fun2
from module2 import* 

def main():
    fun1()
    fun2()
    module2_fun1()
    module2_fun2()

main()


'''
Syntax5: from <module-name> import <identifier> as <alias-name>
This syntax import identifier (function-name,class name, object name)
within current module with alias name.

'''