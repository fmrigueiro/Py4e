fruit = 'banana'
letter = fruit[0]
print(letter)

#printing error
new = 'abc'
print(new[5])

#new function
index = 0
while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1

#easier form
for letter in fruit:
	print(letter)

#looping and counting
count = 0

for letter in fruit:
	if letter == "a":
		count = count + 1
print(float(count))

s = 'Monty Python'

print(s[:1100])

#Manipulating strings

'n' in fruit
if("a" in fruit):
	print("Yeah!!")

print("Hello".lower())

# String Comparison

if word == 'banana':
	print("all right, bananas.")

# Libraries

greet = 'hello Bob'
zap = greet.lower()
print(zap)
print('Hello There'.lower())

# methods on strings
stuff = "Hello world!"
type(stuff)
dir(stuff)

fruit = 'banana'
pos = fruit.find('na')
print(pos)

print(fruit.capitalize())

# Search and replace
greet = "Hello Bob"
nsrt = greet.replace('Bob', 'Jane')
print(nsrt)

# White spaces
greet = '    hello Bob    '
nsrt = greet.lstrip()

# All the built in functions
dir(greet)

# Extracting and Parsing
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
print(atpos)

sspos = data.find(' ', atpos)

# Retrieve the host (the +1 is for starting in 0)
host = data[atpos + 1:sspos]
print(host)

# Chapter 6 Quiz

# 1. what does the following print
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

# 2. what does the following print
x = '40'
y = int(x) + 2
print(y)

# 3. find q
x = 'From marquard@uct.ac.za'
x[8]

# 4. Find uct
x = 'From marquard@uct.ac.za'
x[14:17]

# 5. What is the iteration variable
for letter in 'banana':
	print(letter)

# 6. result of :
print(len('banana') * 7)

# 7. Make upper case
greet = 'Hello Bob'
greet.upper()

# 8. Which one is not a dir
dir(greet)
# shout()

# 9. What will the following Python code print out?

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos + 3])

# Assigment 6
# Write code using find() and string slicing
# (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

num = text.find('0')
print(num)
sspos = len(text)

# Retrieve the host (the +1 is for starting in 0)
host = float(text[atpos + 1:sspos])
print(host)
