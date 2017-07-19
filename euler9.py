#!/usr/bin/python
import sys
import math

def main():
	"""
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

	a2 + b2 = c2
	For example, 32 + 42 = 9 + 16 = 25 = 52.
	
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.
	"""
	
	#we will try to us Euclid's formula of generating pythagorean triplets
	# a = k*(m^2-n^2), b = k * (2mn), c = k*(m^2+n^2)
	#where m, n, and k are positive integers with m > n, and with m and n coprime and not both odd.
	
	#first we try to find a good number of co primes, m and n.  
	#We will stop when we m^2+n^2 >= 998, 
	#the largest possible solution (a = 1, b = 1, c = 998 for this problem) 
	
	coPrimes = [[2,1]]
	index = 0
	
	while 1:
		coPrime = coPrimes[index]
		m=coPrime[0]
		n=coPrime[1]
		
		#branch 1
		m1 = 2*m - n 
		n1 = m
		coPrimes.append([m1,n1])
		
		#branch 2
		m2 = 2*m + n 
		n2 = m
		coPrimes.append([m2,n2])
		
		#branch 3
		m3 = m + 2*n
		n3 = n
		coPrimes.append([m3,n3])
		
		index+=1
		
		if ((math.pow(m,2) - math.pow(n,2)) >= 998):
			break
	
	print coPrimes
	print len(coPrimes)
	print ""
	
	
	#we then go through the list and calculate the pythag triplets
	coPrimes.pop(0)
	for coPrime in coPrimes:
		m=coPrime[0]
		n=coPrime[1]
		k = 1
		while 1:
			
			a = int(k*(math.pow(m,2) - math.pow(n,2)))
			b = k*(2*m*n)
			c = int(k*(math.pow(m,2) + math.pow(n,2)))
			
			#verify
			print coPrime
			print [a,b,c]
			print a+b+c
			if (math.pow(a,2)+math.pow(b,2))==math.pow(c,2):
				#it worked
				None
			else:
				#we messed up somewhere
				raise Exception('We produced an invalid pythag triple')
				None
				
			if a+b+c == 1000:
				print "found it"
				print "the product of a*b*c is: " + str(a*b*c)
				return
				
			k+=1
			
			if (c >998):
				break
		
		
	
if __name__ == "__main__":
    main()
