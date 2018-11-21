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
count = 0
for line in fhand:
	if line.startswith('From:'):
		count = count + 1
print('There were ', count, 'subject lines in ', fname)

# With errors in name use try
fname = input("Input the file name")
try:
	fhand = open(fname)
except:
	print("File cannot be opened", fname)
	quit()
count = 0
for line in fhand:
	if line.startswith('From:'):
		count = count + 1
print('There were ', count, 'subject lines in ', fname)

# Exercise 7.1
# Download words.txt from https://www.py4e.com/code3/words.txt
url = 'https://www.py4e.com/code3/words.txt'

fhand = open('/Users/filipe/Documents/Python Learning/Py4e/Python Data Structures/words.txt')
for line in fhand:
	line = line.rstrip()
	line = line.upper()
	print(line)

# Exercise 7.2
count = 0
fname = open('/Users/filipe/Documents/Python Learning/Py4e/Python Data Structures/mbox-short.txt')
for line in fname:
	if not line.startswith("X-DSPAM-Confidence:"): continue
	count = count + 1
	num = line[len(line) - 7:len(line)]
	num = float(num)
	ave = (num + num) / count
print("Average spam confidence:"
ave)
