import calendar

month,day,year = map(int,input().split())

day_list = ['Mon','Tue','Wed','Tur','Fri','Sat','Sun']

print(day_list[calendar.weekday(year,month,day)])