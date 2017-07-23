#!/usr/bin/python
import math

def main():
	"""
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

	Find the sum of all the primes below two million.
	"""
	#some primes to start out
	primes=[]
	cutoff = 2000000
	
	i=0
	
	#create slieve of erastosthenes
	slieve = range(2, cutoff)
	
	#print slieve
	
	#square root index
	sqrtCutoff = math.sqrt(cutoff) 
	while i < sqrtCutoff:
		j = i
		if(slieve[i] != -1):
			
			while j + slieve[i] < len(slieve):
				j = j + slieve[i]
				#print i, slieve[i], j
				slieve[j] = -1
			
		i+=1
	
	primes = [x for x in slieve if x != -1]
	print primes
	print sum(primes)

if __name__ == "__main__":
    main()
