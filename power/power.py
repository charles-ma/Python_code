#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  power.py
#  This program calculates the power of an integer 
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  

def pow(a,n):
	#this recursive function calculates the value of a**n
	if n == 0:
		return 1
	elif n%2 == 0:
		return pow(a*a,n/2)
	elif n%2 == 1:
		return a*pow(a,n-1)
	else:
		pass
		
a,n = input('Please input the base and power:')
print pow(a,n)
