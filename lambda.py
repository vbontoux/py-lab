
l = lambda x: x*2

print l(2)

mylist = [1,2,3,4,5,6,7,8,9]

print "map"
print map(lambda x: x%2 == 0, mylist)
print map(lambda x: x if x%2 == 0 else 0, mylist)

print "filter"
print filter(lambda x: x%2 == 0, mylist)

print "sorted"
print sorted(mylist, key=lambda x: x, reverse=True)

