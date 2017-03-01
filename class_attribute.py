"""Understanding class / instance attributes"""

class simple: 
    """Old style if running python 2 (make it inherit from object for python 2 new style).
    Inherits from object by default if running python 3.0"""

    class_stuff = "initial class stuff"

    def __init__(self, *args, **kwargs):
        self.instance_stuff = "initial instance stuff"


print simple.__dict__                               # class_stuff="initial class stuff" in the class __dict__
s=simple()
print s.class_stuff                                 # "initial class stuff"
print s.__dict__                                    # no class_stuff in the instance __dict__
s.class_stuff = "Becomes an instance stuff"         
print s.__dict__                                    # class_stuff="Becomes an instance stuff" in the instance __dict__
simple.class_stuff = "Changing the class stuff"     
print simple.__dict__                               # class_stuff="Changing the class stuff" in the class __dict__
print s.__dict__
s=simple()
print s.class_stuff                                 # "Changing the class stuff"

