#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  examScore.py
#  This program is used to convert a score based on 40 into a percentage score
#  Copyright 2012 machao <machao@machao-VGN-FZ15>
#  

print 'The exam had 40 points.'
score =  input('What is your score?')
percent = 100*score/40.0
print 'Your percentage was:',percent
#if percent >= 90:
#	if percent >= 95:
#		print 'You got an A+!'
#	else:
#		print 'You got an A!' 
#	print 'You are doing well in this exam!'
#else:
#	print 'You didn\'t get an A.'
#print 'see you in class next week!'
if percent >= 90:
	print 'You got an A!'
elif percent >= 80:
	print 'You got a B!'
elif percent >= 70:
	print 'You got a C!'
else:
	print 'Your grade is less than a C.'
