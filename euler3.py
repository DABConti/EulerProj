#!/usr/bin/python
import sys

def main():
	num=600851475143
	primes=[1]
	x=2
	while x<num:
		if num%x==0:
			num=num/x
			primes.append(x)
		if num%x==0:
			x-=1
		x+=1
	primes.append(x)
	print 'The primes of the number, 600851475143 are'
	print primes
	
if __name__ == "__main__":
    main()
