# https://stepik.org/lesson/571244/step/7?auth=login&unit=565785

from datetime import datetime, date, timedelta
num = input().split('.')                    # разбиваем ДАТУ на день. месяц. год
x = [input() for i in range(int(input()))]    # список имен и дат рождений
res = []            # список куда будут входить даты подходящие под условие! дата(num) < дат рожд <= дата(num+7)

def exemyear(d, n, r): # d=день рожд, n=дата, r=res функция проверки условий дата(num) < дат рожд <= дата(num+7)
    d2 = d-timedelta(days=7)    # d2 = дата рожд - 7 дней
    if d.month<d2.month:    # если месяц даты рожд < меньше месяца даты рожд -7дней. Например (5.01.20< 29.12.20)
        n1 = n-timedelta(days=365)    # дату уменьшаем на год
        n2 = n+timedelta(days=365)    # дату увеличиваем на год
        if n1 < d <=n2:    # если дата рожд в промежутке
            r.append(d)    # добавляем в res
        return r
    else:                # иначе, оставляем как было не уменьшая и не увеличивая год. т.к он не меняется от 7 дней
        if n < d <= n + timedelta(days=7):
            r.append(d)    # тоже добавляем
            return r

for i in x:        # итерация по датам с именами
    i2 = i.split()[2].split('.')    # 2 раза разбиваем, чтобы получить только дату
    d = date(day=int(i2[0]), month=int(i2[1]), year=int(i2[2]))    # день рожд!
    n = date(day=int(num[0]), month=int(num[1]), year=int(i2[2]))    # дата , НО год как у именинника (меняется)
    exemyear(d, n, res)        # вызов функции для проверки n<d<n+7

if len(res) > 0:    # если список не пуст
    for i in x:     # итерируемся по основному списку, чтобы вывести имя
        if max(res).strftime('%d.%m.%Y') in i:   # макс. дата из списка(самый молодой) переводим в str, в строках
            print(*i.split()[:2])    # выводим имя совпадающее с макс датой из res
else:
    print('Дни рождения не планируются')