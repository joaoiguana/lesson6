numbers = [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    print(number)

count = 10

while count >= 0:
    print("The count is:", count)
    count -= 1

filters = [10, 20, -1, 45, 99, -16, 85, 105, 42]

for filter in filters:
    if filter < 0:
        continue
    if filter > 100:
        break
    print(filter**2)
