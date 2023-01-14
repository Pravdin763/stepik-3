# https://stepik.org/lesson/571244/step/7?auth=login&unit=565785

from datetime import datetime, date, timedelta
num = input().split('.')                    # разбиваем ДАТУ на день. месяц. год
x = [input() for i in range(int(input()))]    # список имен и дат рождений
res = []            # список куда будут входить даты подходящие под условие! дата(num) < дат рожд <= дата(num+7)

def exemyear(d, n, r): # d=день рожд, n=дата, r=res функция проверки условий дата(num) < дат рожд <= дата(num+7)
    d1 = d-timedelta(days=0)        # тажа дата, превращается в нужный формат для вывода month
    d2 = d-timedelta(days=7)
    if d1.month<d2.month:
        n1 = n-timedelta(days=365)
        n2 = n+timedelta(days=365)
        if n1 < d1 <=n2:
            r.append(d1)
        return r
    else:
        if n < d <= n + timedelta(days=7):
            r.append(d1)
            return r

for i in x:
    i2 = i.split()[2].split('.')
    d = date(day=int(i2[0]), month=int(i2[1]), year=int(i2[2]))
    n = date(day=int(num[0]), month=int(num[1]), year=int(i2[2]))
    exemyear(d, n, res)

if len(res) > 0:
    for i in x:
        if max(res).strftime('%d.%m.%Y') in i:
            print(*i.split()[:2])
else:
    print('Дни рождения не планируются')
