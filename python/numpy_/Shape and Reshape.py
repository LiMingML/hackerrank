import numpy

lst = list(map(int, input().split()))
a = numpy.array(lst)
a = numpy.reshape(a, (3,3))
print(a)


