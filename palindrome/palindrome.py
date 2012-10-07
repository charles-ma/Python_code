#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  palindrome.py
#  This program is used to tell whether a string is a palindrome
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  

def palin(s):
	if s == '':
		return True
	else:
		if s[0] == s[-1]:
			return palin(s[1:len(s)-1])
		else:
			return False
			
s = raw_input('Input the string you want to identify as palindrome:')
s1 = ''
#lst = []
for ch in s:
	if 'A'<=ch<='Z':
		ch = ch.lower()
	else:
		pass
	if 'a'<=ch<='z':
		s1 += ch
		#to save memory
		#lst.append(ch)
	else:
		pass
	#s1 = ''.join(lst)
print palin(s1)
