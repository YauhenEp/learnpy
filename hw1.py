import random

for i in range(100):
    print(random.randrange(1, 1000))

numbers = [10, 20, 30, 50, 100, 1, 78, 93, 21, 5, 125, 122, 133]

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