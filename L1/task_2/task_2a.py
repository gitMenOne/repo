#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
i = 1
summa = 0
cub_list = []
cub_index = 0
while i <= 1000:
    if i % 2 != 0:
        cub = i * i * i
        j = i * i * i
        cub_list.append(j)
    i += 1
for cub_number in cub_list:
    div = 999
    sum = 0
    z = cub_number
    while div // 10 != 0:
        mod = cub_number % 10
        div = cub_number // 10
        sum = sum + mod
        cub_number = cub_number // 10
        if div // 10 == 0:
            sum = sum + div
    if sum % 7 == 0:
            summa = summa + z
print(summa)