#printong ASCII function ord

print(ord('H'))
print(ord('i'))

while True:
	data = mysock.recv(512)
	if(len(data) < 1) < 1:
		break
	mystring = data.decode()
mysocket.close()


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
	print(line.decode().strip())

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts=dict()
for line in fhand:
	words = line.decode().strip()
	for word in words:
		counts[words] = counts.get(word, 0) + 1
print(counts)

fhand = urllib.request.urlopen("https://www.stjohnslabs.com/anti-phospho-nfkappab-p65-t505-antibody-stj91119.html")
for line in fhand:
	print(line.decode().strip())

