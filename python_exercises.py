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
while 1:
    print(1)
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


