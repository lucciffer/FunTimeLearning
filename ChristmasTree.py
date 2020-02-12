from random import randint
import os
import shutil
import time

if (os.name == 'nt'):
	import colorama
	colorama.init()

red='\033[0;31m'
green='\033[0;32m'
brworange='\033[0;33m'
yellow='\033[1;33m'
blue='\033[0;34m'
white='\033[1;37m'

def func():
	tlist=['8','0','o','@','*','~','-','+','^','.',',','_','=','{','}',']','[',';',':','#','$','&','!']
	clrs=[yellow,blue,white,red]
	randnum=randint(0, 22)
	if(randnum > 4):
		print(green+tlist[randnum], end = '')
	else:
		print(clrs[randint(0, 3)]+tlist[randnum], end = '')

def christmasTree():
	(cols, lines)=(110,24)
	n=int((lines*9)/10)
	if((n*2)>cols):
		n=int(cols/2)

	if (os.name == 'nt'):
		os.system('cls')
	else:
		os.system("clear")

	i=1
	while i < n:
		k=i;
		width=(cols/2)
		while k < width:
			print(" ", end = '')
			k+=1

		if i == 1:
			print(yellow+"^", end = '')

		j=1
		while j < i:
			func()
			j+=1

		z=1
		while z < i:
			func()
			z+=1

		i+=1
		print("")

	t=0
	while t < (n/10):
		for b in range(int(width-((n/4)+1))):
			print (" ", end = '')
		for c in range(int(n/2)):
			print (brworange+"#", end = '')
		print("")
		t+=1

	while True:
		time.sleep(0.2)
		christmasTree()
		k=i;
		width=(cols/2)
		while k < width:
			print(" ", end = '')
			k+=1

		if i == 1:
			print(yellow+"*", end = '')

		j=1
		while j < i:
				func()
				j+=1

		z=1
		while z < i:
				func()
				z+=1

		i+=1
		print("")

		t=0
		while t < (n/10):
			for b in range(int(width-((n/4)+1))):
				print (" ", end = '')
			for c in range(int(n/2)):
				print (brworange+"#", end = '')
			print("")
			t+=1

while True:
	time.sleep(0.2)
	christmasTree()


"""
This project of Christmas Tree was coded by #Lucciffer
"""
