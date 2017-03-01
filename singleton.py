
""" Singleton patterns
=> Using a simple class decorator
=> Using the metaclass
"""

# Using a simple class decorator

print "=> Using a simple class decorator"
def singleton(cls):
  instances = {}
  def getinstance(*args, **kwargs):
    if cls not in instances:
        instances[cls] = cls(*args, **kwargs)
    return instances[cls]
  return getinstance

@singleton
class MySingle(object):
    def __init__(self, val="init value"):
        self.a_value = val
    def set_a_value(self, val):
        self.a_value = val

c = MySingle()
print c.a_value           # init value
c = MySingle(val="another init value")
print c.a_value           # init value
c.set_a_value(val="now another value")
print c.a_value           # now another value


# Using the metaclass
# => a more regular class construction 

print "=> Using the metaclass"

class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class MySingle2(object):
    __metaclass__ = Singleton
    def __init__(self, val="init value"):
        self.a_value = val
    def set_a_value(self, val):
        self.a_value = val


c = MySingle2()
print c.a_value           # init value
c = MySingle2(val="another init value")
print c.a_value           # init value
c.set_a_value(val="now another value")
print c.a_value           # now another value
