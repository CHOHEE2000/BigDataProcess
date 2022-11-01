#!/usr/bin/python3
import sys

file_path = sys.argv[1]
result_file = sys.argv[2]

f = open(file_path, "rt") 
genrelist = dict()
while True:
	row = f.readline().strip()
	if not row: break

	str = row.split('::')
	if str[2].find('|') != -1:
		genres = str[2].split('|')
		for i in genres:
			if i not in genrelist:
				genrelist[i] = 1
			else:
				genrelist[i] += 1
	else:
		genres = str[2]
		if genres not in genrelist:
			genrelist[genres] = 1
		else:
			genrelist[genres] += 1

f = open(result_file, "wt")
for i, j in genrelist.items():
	s = "{} {}\n".format(i,j)
	f.write(s)
