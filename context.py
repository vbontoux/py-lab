
# Creating a class
class MyContextManager(object):
    def __enter__(self):
        print "Before"
    def __exit__(self, type, value, traceback):
        print "After"


with MyContextManager() as cm:
	print "middle"


# Using a function decorated with @contextmanager
from contextlib import contextmanager
 
@contextmanager
def myfunc():
	try: 
		print "Before"
		yield 
	finally:
		print "After"

with myfunc() as cm:
	print "middle"

