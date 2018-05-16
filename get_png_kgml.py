#!/usr/bin/env python
#coding:utf-8
#20170721

import re
import requests
import sys

kos_file = sys.argv[1]
pnkgml_dir = sys.argv[2]

with open(kos_file,'r')as kos:
	kos.readline()
	for line in kos.readlines():
		ko = line.strip().split('\t')[0]
		print ko
		try:
			png_url = 'http://www.kegg.jp/kegg/pathway/ko/%s.png' %ko
			png_link = requests.get(png_url)
			with open('%s/%s.png' %(pnkgml_dir,ko),'wb')as png:
				png.write(png_link.content)
			kgml_url = 'http://rest.kegg.jp/get/%s/kgml' %ko
			kgml_link = requests.get(kgml_url)
			with open('%s/%s.kgml' %(pnkgml_dir,ko),'wb')as kgml:
				kgml.write(kgml_link.text)
		except:
			print('\t\t\t'+ko)