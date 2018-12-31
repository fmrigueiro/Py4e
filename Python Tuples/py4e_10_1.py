#tuples are not changeble

(x, y) = (4, 'fred')
print(y)

d = dict()
d['csev'] = 2
d['swen'] = 4

for (k,v) in d.items():
	print(k,v)

tups = d.items()

print(tups)


