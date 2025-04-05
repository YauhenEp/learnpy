import random

a = [1,2,4,10,5.6,'string', True]
print(a[5])

print(range(10))
print(range(10, 15))

for i in range(10):
    print(i)

for i in range(10, -10, -3):
    print(i)

print(type(range(10)))
print(type([])) #list
print(type({})) #dict
print(type((1,2,3))) #tupple
print(type(True)) #bool
print(type('tr'))
print(type(10))
print(type(10.00))

numbers = [133, 10, 20, 30, 50, 100, 1, 78, 93, 21, 5, 125, 133]
a = 5
if a == 1:
    print(a)
elif a == 2:
    print(a)
elif a == 3:
    print(a)
else:
    print(a)

if a in numbers:
    print('in list')

maxNumber = 0
for i in range(len(numbers)):
    if numbers[i] > maxNumber:
        maxNumber = numbers[i]

print(maxNumber)

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j+1], numbers[j] = numbers[j], numbers[j+1]

print(numbers)

odd_sum = 0
even_sum = 0
for i in range(len(numbers)):
    if i % 2 == 0:
        even_sum += numbers[i]
    else:
        odd_sum += numbers[i]

print(odd_sum)
print(even_sum)

try:
    1/0
except ZeroDivisionError:
    print("error")

a = "string"

for i in range(len(a)):
    print(a[i])

print(a[1:4])
print(a[-2])
print(a[:-2])

for i in a:
    print(i)

print(a.count('s'))
print(a.count('c'))

b = [1, 4, 7,2,5,6, 10, 11]
b.sort()
print(b)
c = (1, 4, 7,2,5,6, 10, 11)
# c.sort()
d = sorted(c)
print(b)

e = [1, 4, 7,2,5,6, 10, 11]

e.append(8)
print(e)
e.insert(1, 8)
print(e)

removed = e.pop(len(e) - 1)
print(e)
print(removed)
e.reverse()
print(e)

f = [1, 10, 20, 5, 4, 8]
r = f
f.sort()
print(f)
print(r)

y = f.copy()
f.reverse()
print(y)
print(f)
