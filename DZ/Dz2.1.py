number = int(input('Введите число: '))
new_number = 0
result = 0
count = len(number)
for i in number:
    new_number = number - (number % 10)
    result = result + (number - new_number)
    number = number / 10


print(number)
