n = 5
while n > 0:
	print(n)
	n = n-1
print('blastoff')
print(n)


while True:
	line = input("> ")
	if line == "done":
		break
	print(line)
print("Yeah!!")


while True:
	line = input("> ")
	if line[0] == "#":
		continue
	if line == "done":
		break
	print(line)
print("Yeah!!")


for i in [1,2,3,4,5]:
	print(i)
print('blastoff')

friends = ['ana', 'ze', 'pires']
for friend in friends:
	print('Hello', friend)
print('thanks to all')

longest_so_far = -1
print('Before', longest_so_far)
for the_num in [9,41,12,14,74,15,6]:
	if the_num > longest_so_far:
		longest_so_far = the_num
	print(longest_so_far, the_num)
print('After', longest_so_far)

zork = 0
for thing in [3,4,5,7,2,1,5]:
	zork = zork + 1
	print(zork, thing)
print('after', zork)


found = False
print('Before', found)
for value in [2,12,4,5,6,34,3,43,66]:
	if value == 3:
		found = True
		break
	print(found, value)
print('After', found, value)


#Smallest Value
smallest_so_far = -1
print('Before', smallest_so_far)
for the_num in [412,21,44,55,12,2]:
	if the_num < smallest_so_far:
		smallest_so_far = the_num
	print(smallest_so_far, the_num)
print("After", smallest_so_far)


#Correct
smallest_so_far = None
print('Before')
for value in [412,21,44,55,12,2]:
	if smallest_so_far is None :
		smallest_so_far = value
	elif value < smallest_so_far:
		smallest_so_far = value
	print(smallest_so_far, value)
print('After', smallest_so_far)

n = 5
while n > 0 :
    print(n)
print('All done')


#Exercise 5.1

#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters
# anything other than a valid number catch it with a try/except and put out an appropriate message and
# ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        print (num)
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
             smallest = num
    except ValueError:
        print("Please, enter only numbers.")

print ("Maximum", largest)
print ("Minimum", smallest)