a = {"a": 1, "b": 2, "c": 3}
print(a)
print(a['a'])
print(a.get('b'))

a.update({'c': 4})
print(a)

a['b'] = 90
print(a)

b = a.fromkeys([5,6,7], 90)
print(b)

for key, value in b.items():
    print(key, value)