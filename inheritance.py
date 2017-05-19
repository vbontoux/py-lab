class parent1(object):
	def __init__(self, arg):
		super(parent1, self).__init__()
		self.p1 = arg
		

class child1(parent1):
	"""docstring for ClassName"""
	def __init__(self, arg):
		parent1.__init__(self,arg)
		self.c1 = arg

class child2(parent1):
	"""docstring for ClassName"""
	def __init__(self, arg):
		parent1.__init__(self,arg)
		self.c2 = arg


class child3(child1, child2):
	"""docstring for ClassName"""
	def __init__(self, arg):
		child1.__init__(self,arg)
		child2.__init__(self,arg)
		self.c3 = arg

c= child3(1)

print c.__dict__