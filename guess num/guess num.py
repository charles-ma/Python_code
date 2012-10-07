#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  guess num.py
#  This program is for a number guess in Chapter2.25, exploring python
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  




import random
n = random.randint(1,100)
while True:
	m = input('input here:')
	if m == n:
		print 'you are right'
		break
	elif m>n:
		print 'too high'
	elif m<n:
		print 'too low'
	else:
		pass

