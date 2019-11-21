## Exercises for Python basics

# Exercise 1
# Subex 2
b=3
c=4
a=(b**2 + c**2)**0.5
# Subex 3
print(type(a)) #<class 'float'>
print(type(b)) #<class 'int'>

# Exercise 2
# Subex 1
# while 1:
#    print(1)
# Subex 2
gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0
while count < 4:
    item = gases[count]
    print(item, count)
    count +=1
# Subex 3
name = "Lisa"
if name == "Lisa":
    print(name + " plays saxophone")
elif name == "Bart":
    print(name + " rides skateboard")
else:
    print(name + " lives in springfield")
# Subex 4
x = 1 # Or: 22.1, "hello", [1,2], 0, 0.0, None, False
if x: print(x, " is True")

# Exercise 3
# Subex 1
x = list(range(1,6)) #creates list from 1 to 5, range alone doesn't do it!
# Subex 3
forward = []
backward = []
values = ["a", "b", "c"]
for val in values:
    forward.append(val)
    backward.insert(0,val)
print(forward,backward)
forward.reverse()
print(forward==backward) #compare lists
# Subex 4
dir(forward) # gives all methods that can be done with that object
# Extra
while forward:    # does the same as while len(forward) > 0:
    forward.pop()
    print(forward)

# Exercise 4
# Subex 1
t = (1,) #creates tuple with one element
tup = tuple(range(100,201)) #builds a tuple from a range
# Subex 2
mylist = [23, "hi", 2.4e-10]
for (count, item) in enumerate(mylist): # enumerate creates tuples of positions and list items
    print(count, item)
# Subex 3
first, middle, last = mylist #unpacks values from list in variables
first, middle, last = middle, last, first #re-assigns values of variables

# Exercise 5
# Subex 1
with open('weather.csv', 'r') as reader: #reading in the file
    data = reader.read()                 #storing content in data
print(data)
# Subex 2
with open('weather.csv', 'r') as reader:
    data = reader.readline()
    print(data)
    while data:
        data = reader.readline()
        print(data)
    print('its over')
# The following does the same but more elegant:
with open('weather.csv', 'r') as reader:
    while True:
        data = reader.readline()
        if not data:
            break
        print(data)
    print('its over')
# Subex 3
with open('weather.csv','r') as reader:
    data = reader.readline()
    rain = []
    for line in reader.readlines():
        rain.append(float(line.strip().split(",")[-1]))
        # strip removes linebreaks and spaces, split produces list splitted at ,
print(rain)
with open('myrain.txt','w') as writer:
    writer.write(str(rain)) # write can only write strings

# Exercise 6
# Subex 2
s = "I love to write python"
split_s = s.split() # does the same as s.split(' ')
for word in split_s:
    if word.lower().find('i') > -1:
        print(f'I found \'i\' in \'{word}\'')
# f before string allows to fill in variable in { }
# Subex 3
something = 'Completely Different'
something.find('plete') #finds first position of substring 'plete'
thing2 = something.replace('Different','Silly') # replace 'Different'

# Exercise 7 - Aliasing
liste = [[1,2,3],[4,5,6]]
sublist = liste[0]
sublist[1] = 'hello' #this changes both sublist and list
liste[0][1] = 2 #changes BOTH back
# Avoid this by using copy.deepcopy
import copy
sublist2 = copy.deepcopy(liste[0])
sublist2[1] = 'hello' #changes now just sublist2, not list

# Exercise 8
# Subex 1
def double_it(number):
    return number*2
# Subex 2,3
def calc_hypo(a,b):
    if type(a) not in (float,int) or type(b) not in (float,int):
        print('Wrong argument type!')
        return False
    if a < 0 or b < 0:
        print('Argument negative!')
        return False
    hypo = (a**2 + b**2)**(1/2)
    return hypo
print(calc_hypo(3,4))

# Exercise 9
# see created folders and file, also directory TestLib and testfile.py

# Exercise 10
# Subex 1
a = set([0,1,2]) #creates a set
# Subex 2
band = ['mel','geri','victoria','mel','emma']
counts = {} #creates empty dictionary
for member in band:
    if member not in counts:
        counts[member] = 1
    else:
        counts[member] += 1

for entry in counts:
    print(entry,counts[entry])

# Exercise 11
# didn't do that



## Exercises for Python Numpy
import numpy as np

# Exercise 1
# Subex 1
a1 = np.array(range(1,11),np.int32) # creates an array of integers
b1 = a1.astype(np.float32) # creates new array b1 with changes type
a2 = np.array(range(1,11),np.float32) # array of floats
print(a1.dtype) # shows type of array

# Exercise 2
# Subex 1
arr = np.array((list(range(4)),list(range(10,14))))
arr.shape # this works not for all methods!
np.shape(arr) # both give the shape, same for a lot of methods in numpy

# Exercise 3
# Subex 2
arr = np.array(range(0,10))
arr < 3 # returns boolian type array, same as:
np.less(arr,3)
# array([ True,  True,  True, False, False, False, False, False, False, False])
arr[arr < 3] # returns array with entries which give True in arr < 3:
# array([0, 1, 2])
condition = np.logical_or(arr < 3 , arr > 8) # gives array of boolians
np.where(condition, arr * 5, arr * -5) # gives array where the second argument is applied to entries that match condition, otherwise the third
# Subex 3
def wind_magnitude(u, v, min_val = 0.1):
    "Function that takes arrays u,v and calulates the total magnitude"
    mag = (u**2 + v**2)**0.5
    output = np.where(mag < min_val, min_val, mag)
    "Here it replaces all entries smaller min_val with min_val"
    return output

# Exercise 4
import numpy.ma as MA7
# Subex 1
# MA.masked_array(data=[], mask=[], fill_value = )
marr = MA.masked_array(range(10), fill_value = -999)
print(marr, marr.fill_value)
marr[2] = MA.masked # mask the third value
# Create masked array equal to marr where marr is <7:
narr = MA.masked_array(marr, marr > 6)
#OR:
narr = MA.masked_where(marr > 6, marr)
x = MA.filled(narr) # filles masked array with fill_value, gives an array
# Subex 2
m1 = MA.masked_array(range(1,9))
m2 = m1.reshape(2,4)
m3 = MA.masked_where(m2 > 6, m2) #OR:
m3 = MA.masked_greater(m2, 6)






