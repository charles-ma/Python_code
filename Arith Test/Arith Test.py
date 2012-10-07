#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Arith Test.py
#  This program is for tutors of arithmetics to test their students 
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  

#  
#  
import random
right = 0
for i in range(1,11):
	m = random.randint(0,9)
	n = random.randint(0,9)
	sum = m+n
	answer = input('What is '+str(m)+' and '+str(n)+' ?')
	if sum == answer:
		right += 1
	else:
		pass
print 'Your score is',right*10
