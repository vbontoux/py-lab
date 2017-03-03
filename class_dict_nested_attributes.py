"""
We want to access nested dict items using the class attribute dot separated access: a.b.c
"""

# Let's consider that our data is only made of dict of string values to simplify

class str_(str):
    def __init__(self, string):
        super(str_, self).__init__(string)

    def __getattr__(self, name):
        print name
        return AttrDict()
    

class AttrDict(dict):

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)
    
    # Overloaded to make sure the __init__ loops through the args calling __setitem__ and therefore change the dicts into AttrDict
    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).iteritems():
            self[k] = v

    def __getitem__(self, key):
        val = dict.__getitem__(self, key)
        return val

    # Here we decide to replace various type with types that can be access with unknown attributes like AttrDict and str_
    def __setitem__(self, key, val):
        if isinstance(val, dict):
            dict.__setitem__(self, key, AttrDict(val))
        elif isinstance(val, str):
            dict.__setitem__(self, key, str_(val))
        else:
            dict.__setitem__(self, key, val)

    def __setattr__(self, attr, value):
        self[attr] = value

    def __getattr__(self, name):
        print name
        if name in self:
            return self[name]
        else:
            return AttrDict()
    
    # Orverload the copy since we have changed the setitem, the default  copy does not work
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.update(self)
        return result

    def __deepcopy__(self, memo):
        from copy import deepcopy
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.items():
            setattr(result, k, deepcopy(v, memo))
        return result



m = AttrDict(a_dict={"a_sub_string":"Hello"}, a_string="World")

print m.a_dict.a_sub_string              # a_dict has been converted into an AttrDict and therefore allow .dot access to a_sub_string 
print m.a_dict.undefined_var             # undefined_var does not exist but is actually created as an empty AttrDict by a_dict
print m.a_string.undefined_var            # undefined_var if created as an empty AttrDict by str_
print m.a_string.undefined_var.undefined_var       # so on so forth ...

# output:
# a_dict
# a_sub_string
# Hello
# a_dict
# undefined_var
# {}
# a_string
# undefined_var
# {}
# a_string
# undefined_var
# undefined_var
# {}

