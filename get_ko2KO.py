#!/usr/bin/env python
#coding:utf-8
#20170721

import re
import requests
import sys

out_file = sys.argv[1]
out = open(out_file,'w')
out.write('ko\tdescript\tKOs\n')

kos_url = 'http://www.kegg.jp/kegg/pathway.html'
kos_link = requests.get(kos_url)
kos_data = kos_link.text

ko_2desc = re.findall(r'<dt>(\d\d\d\d\d)</dt><dd><a href=".*?">(.*?)</a></dd>',kos_data)
for i in range(len(ko_2desc)):
	ko = ko_2desc[i][0]
	desc = ko_2desc[i][1]
	ko2KO_url = 'http://rest.kegg.jp/link/ko/ko%s' %(ko)
	ko2KO_link = requests.get(ko2KO_url)
	ko2KO_text = ko2KO_link.text
	KOs = re.findall('ko:(K\d\d\d\d\d)',ko2KO_text)
	print('%s\t%s\t%s\n' %(ko,desc,';'.join(KOs)))
	out.write('ko%05d\t%s\t%s\n' %(int(ko_2desc[i][0]),desc,';'.join(KOs)))
	out.flush()

out.close()	