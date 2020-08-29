# -*- coding: utf-8 -*-
s = "wepewomwelqasÃ±leoiakrtui"
vowels = ["a","e","i","o","u"]
noVowels = 0

for vowels in s: 
   	if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels == 'u':
	   noVowels += 1
print 'Number of vowels: ' + str(noVowels)

s = 'azcbobobegghakl'
txtBob = ''
cuenta = 0

if txtBob in s:
    print "Si esta"
    for txtBob in s:
		txtBob = 'bob'
    cuenta += 1
print cuenta 
    
#print 'Number of times bob occurs is: ' + str(s.find(txtBob))

import sys

def contar(string, letra):
	contador, string, letra = 0, string, letra
	try:
		letra = letra.split()
	except:
		letra = [letra]
	for d in letra:
		exec("contador_%s = 0"%d)
	for i in string:
		for h in letra:
			if i == h:
				exec("contador_%s += 1"%h)
	for x in letra:
		exec("print 'Letra %s', contador_%s" % (x, x))

contar("Javiera", "a v")
