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

