#!/usr/bin/python
import sys

def main():
	x=20 
	small=0
	i=0
	while small==0 :
		for i in range(1,21):
			print x
			print i
			if (x%i)!=0:
				
				break
			if i==20:
				small=x
		i=0
		x+=1
	print 'The smallest int divisable by 1-20 is:'
	print small
		
	


if __name__ == "__main__":
    main()
