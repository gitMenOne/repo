#Вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
duration = int(input("duration = "))

if duration < 60:
    print(duration, "сек")
elif duration < 3600:
    minute = duration // 60
    sek = duration % 60
    print(minute, "мин", sek, "сек")
elif duration < 86400:
    hour = duration // 3600
    minute = (duration % 3600) // 60
    sek = duration % 60
    print(hour, "час", minute, "мин", sek, "сек")
elif duration >= 86400:
    day = duration // 86400
    hour = (duration % 86400) // 3600
    minute = (duration % 3600) // 60
    sek = duration % 60
    print(day, "дн", hour, "час", minute, "мин", sek, "сек")
