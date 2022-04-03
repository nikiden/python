duration = int(input('введите время в секундах:' ))
second = duration % 60
minute = 60
hour = minute * 60
day = hour * 24
if duration < minute:
    print(duration, 'сек')
elif duration < hour:
    print(duration // minute, 'мин', duration % minute, 'сек')
elif duration < day:
    print(duration // hour, 'час', duration % hour // minute, 'мин', duration % minute, 'сек')
else:
    print(duration//day, 'дн', duration % day // hour, 'час', duration % hour // minute, 'мин', duration % minute, 'сек')