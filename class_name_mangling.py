"""Private members don't exist in python but there is a convention (PEP 8 -- Style Guide for Python Code -- http://www.python.org/dev/peps/pep-0008/):
_single_leading_underscore: weak "internal use" indicator. E.g. "from M import *" does not import objects whose name starts with an underscore.
__double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo)
"""

class MyClass(object):
    """Example of name mangling"""
    def my_funtion(self):
        print "original funtion"

    __a_private_class_attribute = "This is a private attribute"
    __my_original_function = my_funtion


class ChildClass(MyClass):

    def my_funtion(self):
        print "child function"


# Accessing the private member requires to use the name mangling
p = MyClass()
p.my_funtion()
print p._MyClass__a_private_class_attribute + " => p._MyClass__a_private_class_attribute works"
try :
	print p.__a_private_class_attribute
except:
	print "p.__a_private_class_attribute fails..." 
p.__a_private_class_attribute = "This is a simple new object attribute"
print p.__a_private_class_attribute


c = ChildClass()
c.my_funtion()						# Calling the overloaded function 
c._MyClass__my_original_function()	# Calling the original function

