#!/usr/bin/python
def main():
	primes=[]
	x=15
	i=0
	while primes[len(primes)-1]<100000:
		while i< len(primes):
			if x%primes[i]==0:
				break;
			i+=1
			if i==len(primes):
				primes.append(x)
		i=0
		x+=2
	print primes[len(primes)-1]
	

if __name__ == "__main__":
    main()
