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


(0,1,2) < (5,1,2)


d['zaquis'] = 22
d['jjs1'] = 1

sorted(d.items())

for k,v in sorted(d.items()):
	print(k, v)

c = d
tmp = list()
for k, v in c.items():
	tmp.append((v,k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


c = {'a':10, 'b':5, 'c':22}

print(sorted([(v,k) for k,v in c.items()]))

c = tuple()

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

