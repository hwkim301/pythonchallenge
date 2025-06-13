from datetime import date
from calendar import isleap
for year in range(1006,2006,10):
    if (isleap(year) and date(year,1,26).weekday() == 0):
        print(year)