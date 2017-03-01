
# using the iter function

mylist = ["a", "b", "c", "d"]

it = iter(mylist)


while True:
	try:
		print it.next()
	except StopIteration, e:
		break


# Creating an iterator class from scratch

class myitclass:
	def __init__(self, word):
		self.word = word
		self.c = 0

	def __iter__(self):
		return self

	def next(self):
		if self.c < len(self.word):
			ret = self.word[self.c]
			self.c += 1
			return ret, str(self.c-1)
		else:
			raise StopIteration()

it = myitclass("vincent")

while True:
	try:
		print it.next()
	except StopIteration, e:
		break


# using a generator to create an iterator
def mygen(word):
	print "starting"
	for w in word:
		yield w
	print "the end"

for m in mygen("Bonjour"):
	print m


