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

#methods on strings

stuff = "Hello world!"
type(stuff)

dir(stuff)

# String Comparison

if word == 'banana':
	print("all right, bananas.")
