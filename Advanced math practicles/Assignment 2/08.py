# Write a python program to extract year , month , date and time using lambda   

import datetime

now = datetime.datetime.now()

year = lambda x : (x.year)
month = lambda x : (x.month)
date = lambda x : (x.date())
time = lambda x : (x.time())

def disp():
    print(f"Year :- {year(now)} \nMonth :- {month(now)} \nDate :- {date(now)} \nTime :- {time(now)}")

disp()