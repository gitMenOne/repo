#Реализовать склонение слова «процент» во фразе «N процентов».
#Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
i = 1
procent = [1, 21, 31, 41, 51, 61, 71, 81, 91]
procenta = [2, 3, 4, 22, 23, 24, 33, 34, 32, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
procentov = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99, 100]
while i <= 100:
    for p in procent:
        if i == p:
            print(i, " процент")
    for z in procenta:
        if i == z:
            print(i, " процента")
    for x in procentov:
        if i == x:
            print(i, " процентов")
    i += 1