
x = 5
if x == 5:
    print('x is 5')
    print('still 5')
    print('third 5')
print('aftewards of 5')


for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('done with i', i)
print('All Done')

x = 42
if x > 1:

    print('more than 1')
    if x > 100:
        print("bigger than 100")
print('all done')

astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -12

print('first', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -12
    
    
rawstr = input('enter a number: ')
try: 
    ival = int(rawstr)
except: 
    ival = -1    
if ival >0 :
    print('nice work')
else: 
    print('not a number')
    
####################
    
score = input("Enter Score: ")

try:
    value = float(score)
except:
    value = -1
if 0 < value < 0.6:
    print("F")
elif  0.6 <= value < 0.7:
    print("D")
elif 0.7 <= value < 0.8:
    print("C")
elif 0.8 <= value < 0.9:
    print("B")
elif value >= 0.9:
    print("A")
else:
    print("Please use a correct number")

