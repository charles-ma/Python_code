#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dec2hex.py
#  This program converts decimal numbers into hexadecimal ones
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  
#  
def converter(n):
	#this function converts decimals to hexadecimals
	if n < 10:
		return str(n)
	elif n == 10:
		return 'A'
	elif n == 11:
		return 'B'
	elif n == 12:
		return 'C'
	elif n == 13:
		return 'D'
	elif n == 14:
		return 'E'
	elif n == 15:
		return 'F'
	else:
		return converter(n/16)+converter(n%16)

def converter1(n):
	#this function converts decimals to binaries
	if n < 2:
		return str(n)
	else:
		return converter1(n/2)+converter1(n%2)
		
n = input("please input the number you want to convert into hex(binary):")
print converter(n)+'('+converter1(n)+')'


