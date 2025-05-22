data = set('hello')
print(data)

new_data = {1, 7, 4, 0}
print(new_data)

new_data.add(5)
print(new_data)
new_data.discard(5)
print(new_data)
new_data.update([0, '12', True, 1])
print(new_data)

nums = [19, 1, 0 ,8, 9, 10, 1, 1, 0]
print(nums)
new_nums = set(nums)
print(new_nums)
print(list(new_nums))

new_set = frozenset(nums)
print(new_set)

