#!/usr/bin/python
#-*- encoding: UTF-8 -*-
# Trier liste des repo dans readme du repo ListeRepos


def str_trim(string) :
	while '\t' in string :
		string = string.replace("\t", ' ')

	while '  ' in string :
		string = string.replace("  ", ' ')

	return string





file = 'readme.txt'
output = 'output.txt'
#output = 'readme.txt'
tmp = []
to_be_sorted = dict()
header = '# Liste des Repos disponibles\n\n'

#data = [x.replace('\r\n', '').replace('\n', '') for x in open(file, 'r')]
data = [x for x in open(file, 'r')]
max_size = 0
dico = dict()
links = []

for d in data :
	if d.startswith('- '):
		str1 = str_trim(d.split(':')[0])
		if len(d.split(':')) > 1 :
			str2 = ':'.join(d.split(':')[1:])
		else :
			str2 = ''
		size = len(str1)
		dico[str1] = [size, 0, str_trim(str2)]    # dico[nutridata] = [size str, offset, reste]
		if size > max_size :
			max_size = size
	if d.startswith('https'):
		links.append(d)
	

for key in dico.keys() :
	dico[key][1] = max_size - dico[key][0] + 1



with open(output, 'w') as fs:
	fs.write(header)
	for key in dico.keys():
		offset = dico[key][1]
		str2 = dico[key][2]
		fs.write("%s%s.%s" % (key, offset * '.', str2))
	fs.write('\n\n')
	fs.write(''.join(links))
	fs.close()