"""Understanding class copy"""

class simple: 
    class_stuff = "initial class stuff"

    def __init__(self, *args, **kwargs):
        self.instance_stuff = "initial instance stuff"
        self.a_dict = dict(*args,**kwargs)




s=simple()
from copy import copy, deepcopy
s1 = copy(s)
print s1.__dict__
s=simple({"name": "value", "sub_dict": {"sub_name": "sub_value"}})
print str(id(s))
print id(s.a_dict)
print id(s.a_dict['sub_dict'])
s1 = copy(s)
print id(s1)						# different object address
print id(s1.a_dict)					# same
print id(s1.a_dict['sub_dict'])		# same 
s1 = deepcopy(s)
print id(s1)						# different object address
print id(s1.a_dict)					# different
print id(s1.a_dict['sub_dict'])		# different

