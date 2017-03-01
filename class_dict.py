"""
We want to have a class that behaves like a dict.
we actually want to manipulate an object like a dictionnary and as well be able
to access its attributes with the usual dot like: myobj.myattribute
"""

class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)


m = AttrDict(a="Hello", b="World")

print m.a
print m.b
