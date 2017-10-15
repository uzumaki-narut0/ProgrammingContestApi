from dateutil.parser import parse
from datetime import datetime
obj = parse("2017-10-15T20:30:00+05:30")
print(obj.strftime("%A %d %B %Y"))
a = 2
b = ['a', 'b', 'c']
print(type(a))
if(str(type(a)) == "<class 'int'>"):
	print(b[:a+1])