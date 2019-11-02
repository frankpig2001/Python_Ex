import sys
print(sys.executable)

# test reading lines from an open file
a = open("C:\\Users\\Frank\\Documents\\code\\Python\\App\\List_of_IPs.txt")
print(a.readlines())
# print(list(a))
a.seek(0)
for i in a.readlines():
	i.rstrip('\n')
	print(i)

a.seek(0)

c = a.readlines()[0].rstrip("\n").split(".")
print(list(c))
a.seek(0)
d = a.readlines()[1].rstrip("\n").split(".")
print(list(d))
a.seek(0)
e = a.readlines()[2].rstrip("\n").split(".")
print(list(e))