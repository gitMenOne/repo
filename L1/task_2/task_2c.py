
#Решить задачу под пунктом b, не создавая новый список
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
i = 1
summa = 0
while i <= 1000:
    if i % 2 != 0:
        cub = i * i * i + 17
        j = i * i * i + 17
        div = 999
        sum = 0
        while div // 10 != 0:
            mod = j % 10
            div = j // 10
            sum = sum + mod
            j = j // 10
            if div // 10 == 0:
                mod = j % 10
                sum = sum + mod
        if sum % 7 == 0:
            summa = summa + cub
    i += 1
print("+ 17 к каждому элементу списка: ", summa)