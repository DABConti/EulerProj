#!/usr/bin/python

def main():
	x=999
	y=999
	z=1
	largest=0
	while y>99:
		if isPalindrome(x*y):
			if (x*y)>largest:
				largest=(x*y)
			
		# better if i use diagionalization to find products
		x-=1
		if x<100:
			y-=1
			x=999
		
	print largest
	

def isPalindrome(x):
	nums=[]
	y=x
	z=100000
	while z>=1:
		a=y/z
		nums.append(a)
		y=y-z*a
		z=z/10
	if x<100000:
		nums.pop(0)
	print nums
	while len(nums)>0:
		if len(nums)==1:
			return True
		a=nums.pop(0)
		b=nums.pop()
		if a!=b:
			return None
	
	return True

if __name__ == "__main__":
    main()
