date=raw_input('\n enter a year in dd-mm-yyyy format \n ')

year=int(date[6:10])
print  year

if year%4==0: #it should be divisible by 4
	if year%100==0: #if it is  divisible by 100 then
		if year%400==0: # must be divisible by 400.
			print 'year is leap year'
		else:
			print 'year is not leap year'
	else:#if not divisible by 100 it is suffiecient to divisible by 4.
		print 'year is leap year'
else:
	print 'year is not leap year'


