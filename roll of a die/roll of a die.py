#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  roll of a die.py
#  This program simulates the game of Chapter2.24, exploring python
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  

import random
raw_input('continue?')
i = random.randint(1,6)
j = random.randint(1,6)
sum = i+j
print i,j,sum
if sum == 7 or sum == 11:
	print 'win'
elif sum == 2 or sum == 3 or sum == 12:
	print 'lose'
else:
	point = sum
	while True:
		raw_input('continue?')
		i = random.randint(1,6)
		j = random.randint(1,6)
		sum = i+j
		print i,j,sum
		if sum == 7:
			print 'lose'
			break
		elif sum == point:
			print 'making the point'
			break
		else:pass


