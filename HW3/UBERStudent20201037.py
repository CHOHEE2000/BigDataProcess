#!/usr/bin/python3
import sys
import calendar

uber_file = sys.argv[1]
result_file = sys.argv[2]
weekdayCode = ['MON','TUE','WED','THU','FRI','SAT','SUN']

f = open(uber_file, "rt")
output = dict()
while True:
	row = f.readline().strip()
	if not row: break

	uberList = row.split(',')
	date = uberList[1].split('/')
	day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))

	key = uberList[0]+","+weekdayCode[day]
	val = [int(uberList[2]), int(uberList[3])]
	print(key, val)
	if key not in output:
		output[key] = val
	else:
		valList = output.get(key)
		valList[0] += val[0]
		valList[1] += val[1]
		output[key] = valList

f = open(result_file, "wt")
for i, j in output.items():
	v = str(j[0]) + "," + str(j[1])
	s = "{} {}\n".format(i,v)
	f.write(s)

f.close()
