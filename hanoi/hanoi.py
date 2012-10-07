#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hanoi.py
#  This program is used to solve the Hanoi proble
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  

def hanoi(n,x,y,z):
	#n is the number of disks, x is the initial pole, y is the target pole and z is the temporary pole
	if n == 1:
		print x+'-->'+y
	else:
		hanoi(n-1,x,z,y)
		print x+'-->'+y
		hanoi(n-1,z,y,x)

n = input('input the number of disks:')
hanoi(n,'A','B','C')
