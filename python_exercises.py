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
list = [[1,2,3],[4,5,6]]
sublist = list[0]
sublist[1] = 'hello' #this changes both sublist and list
list[0][1] = 2 #changes BOTH back
# Avoid this by using copy.deepcopy
import copy
sublist2 = copy.deepcopy(list[0])
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






    


