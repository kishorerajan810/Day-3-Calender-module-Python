import datetime

a,b,c =map(int,input("enter :").split())
intDay = datetime.date(year=c, month=a, day=b).weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[intDay].upper())
