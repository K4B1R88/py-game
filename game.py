#!/usr/bin/env python
# encoding: utf-8
"""
game.py

Created by HaCode on 30/08/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""


###  Stone Paper Sizer  ####
###            Game            ####


import random

def  mygame(comp,you):
	if (comp == you):
		return None
	elif comp == 'r':
		if you == 'p':
			return True
		elif you == 's':
			return False
	elif comp == 'p':
		if you == 's':
			return True
		elif you == 'r':
			return False
	elif comp == 's':
		if you == 'r':
			return True
		elif you == 'p':
			return False



print("                   Rock Paper Sizer")
print("                      *_Game_*")	
print("              Rock < Paper < Sizer < Rock ")
print()
print()
print("[*] Comp Turn : Rock(r) Paper(w) and Sizer(s) ")
randNo = random.randint(1,3)
if randNo == 1:
	comp = 'r'
elif randNo == 2:
	comp = 'p'
elif randNo == 3:
	comp = 's'
	
you = input("[*] Your's Turn : Rock(r) Paper(p) and Sizer(s) ")

print(f"Compture Chose {comp}")
print(f"You Chose {you}")


a = mygame(comp,you)
if a == None:
	print("The Match is Tie")
elif a == True:
	print("You Won The Match")
elif a == False:
	print("You Lose!")