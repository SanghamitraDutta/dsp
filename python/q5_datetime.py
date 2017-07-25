# Hint:  use Google to find python function

####a) 
from datetime import datetime 

date_start = '01-02-2013'  
date_stop = '07-28-2015' 

a=datetime.strptime(date_start,'%m-%d-%Y')
b=datetime.strptime(date_stop,'%m-%d-%Y')

delta=b-a
print(a)
print(b)
print(delta.days)


####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
