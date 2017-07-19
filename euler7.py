#!/usr/bin/python
def main():
	primes=[2,3,5,7,11,13]
	x=14
	i=0
	while len(primes)<10001:
		while i< len(primes):
			if x%primes[i]==0:
				break;
			i+=1
			if i==len(primes):
				primes.append(x)
		i=0
		x+=1
	print primes
	print primes[10000]

if __name__ == "__main__":
    main()
