# Python data Structures
# Loading files

xfile = open('/Users/filipe/Documents/Python Learning/Py4e/Python Data Structures/mbox.txt')

for cheese in xfile:
	print(cheese)

fhand = open('/Users/filipe/Documents/Python Learning/Py4e/Python Data Structures/mbox.txt')
inp = fhand.read()
# Length of the string
print(len(inp))

print(inp[:20])

# Searching for Specific text in file

for line in fhand:
	if line.startswith('From: '):
		print(line)

# striping the new line (\n)
# rstrip takes away the whitespace
fhand = open('/Users/filipe/Documents/Python Learning/Py4e/Python Data Structures/mbox.txt')
for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)

#Using continue
fhand = open('/Users/filipe/Documents/Python Learning/Py4e/Python Data Structures/mbox.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From:'):
		continue
	print(line)


#Using an input for the different Files
fname = input("Input the file name")
fhand = open(fname)
