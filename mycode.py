# date-of-birth-assigment
Assignment
import calendar
from datetime import datetime
a=datetime.now()
b=a.date()
c=list(str(b))
d=int(c[0]+c[1]+c[2]+c[3])
e=input('Enter your age: ')
f=int(d)-int(e)
g=input('Enter the month: ')
h=input('Enter the date of the month: ')
i=calendar.weekday(int(f),int(g),int(h))
day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
month=['january','february','march','april','may','june','july','august','september','october','november','december']
print('You where born on ',day[i],h, month[int(g)-1], f)


