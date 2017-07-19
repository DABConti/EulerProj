#!/usr/bin/python
def main():
	primes=[2,3,5,7,11,13]
	x=14
	i=0
	while primes[len(primes)-1]<2000001:
		while i< len(primes):
			if x%primes[i]==0:
				break;
			i+=1
			if i==len(primes):
				primes.append(x)
		i=0
		x+=1
	print primes[len(primes)-1]
	

if __name__ == "__main__":
    main()
