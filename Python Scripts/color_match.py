#!/usr/bin/env python3
	# class User():

	# 	preference = 2
	# 	#use User.preference = 0,1,2 when setting value
	# 	#0-bright
	# 	#1-dark
	# 	#2-no choice
	# 	#default no choice

def colorMatch(p,c,t):

	c1 = 0 #c1 is the color of the "matched" clothing
	t1 = 1 #t1 is the type of the "matched" clothing

	#c is the color code of the outfit
		#0-white, 1-black, 2-gray, 3-dark, 4-pastel, 5-bright
	#t is the type of clothing
		#0-tops, 1-pants
	#p is the user's preference
		#0-bright, 1-dark, 2- no choice

	if t==1:
		t1==0 
	else:
		t1==1

	#if user prefers bright outfits
	if p==0:
		if c==0:
			c1 = [0,5,4]
		elif c==1:
			c1 = [5,4,0]
		elif c==2:
			c1 = [5,4,0]
		elif c==3:
			c1 = [5,4,0]
		elif c==4:
			c1 = [4,5,1]
		elif c==5:
			c1 = [0,2,4]

	#if user prefers dark outfits
	if p==1:
		if c==0:
			c1 = [3,2,1]
		elif c==1:
			c1 = [2,3,0]
		elif c==2:
			c1 = [1,3,0]
		elif c==3:
			c1 =[1,0,5]
		elif c==4:
			c1 = [1,2,3]
		elif c==5:
			c1 = [1,2,3]

	#if user prefers neutral outfits
	if p==2:
		if c==0:
			c1 = [5,4,3]
		elif c==1:
			c1 = [5,4,3]
		elif c==2:
			c1 = [1,2,4]
		elif c==3:
			c1 = [1,2,4]
		elif c==4:
			c1 = [0,1,2]
		elif c==5:
			c1 = [1,0,2]

	return(c1,t1)
	# print(c1[0])
	# print(t1)


