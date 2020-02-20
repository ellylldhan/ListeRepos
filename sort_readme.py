#!/usr/bin/python
#-*- encoding: UTF-8 -*-
# Trier liste des repo dans readme du repo ListeRepos

file = 'README.md'
#output = 'output.md'
output = 'README.md'
tmp = []
to_be_sorted = dict()

#data = [x.replace('\r\n', '').replace('\n', '') for x in open(file, 'r')]
data = [x for x in open(file, 'r')]

for d in data :
	if d.startswith('- [**'):
		to_be_sorted[d.lower()] = d
	elif d not in tmp :
		tmp.append(d)
	

for key in sorted(to_be_sorted.keys()):
	# print(key)
	tmp.append(to_be_sorted[key])


with open(output, 'w') as fs:
	fs.write(''.join(tmp))
	fs.close()