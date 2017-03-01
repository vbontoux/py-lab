
# function decorator
def minmaxdeco(max=100):
	def inner(func):
		def wrapper(a, b):
			res = func(a,b)
			return res if res <= max else max
		return wrapper
	return inner

@minmaxdeco(max=10)
def a_simple_function(a, b):
	return a+b


print a_simple_function(1,2)
print a_simple_function(19,2)


# equivalent without decoration 
def a_simple_function2(a, b):
	return a+b

a_new_function = minmaxdeco(max=15)(a_simple_function2)

print a_new_function(1,2)
print a_new_function(15,2)


# class decorator
class minmaxdecoclass():
	def __call__(self, max=100):
		def inner(func):
			def wrapper(a, b):
				res = func(a,b)
				return res if res <= max else max
			return wrapper
		return inner

mmc = minmaxdecoclass()

@mmc(max=10)
def a_simple_function3(a, b):
	return a+b

print a_simple_function3(1,2)
print a_simple_function3(19,2)
