#!/usr/bin/python3
import sys
def main(args):
	if len(args) != 2:
		a = input("Enter Limit : ")
		#print("Enter Argument... as -l limit")
		#exit(4)
	elif args[0] == '-l':
		pass
	else:
		print("Enter Argument.. as -l limit")
		exit(2)
	try:
		a = args[1]
	except:
		pass
	if a== '':
		print("Invalid Argument...")
		exit(5)
	elif a.isdigit():
		a = int(a)
	elif a[0] == '-' and a[1:].isdigit():
		print("Negative Number Not Allowed")
	else:
		print("Invalid Argument")
		exit(4)
	print("a sorted list (ascending order) of all the prime numbers between 2 and "+str(a)+" (including 2 but not including "+str(a)+") ")
	primes = []
	for n in range(2,a):
		prime = True
		for p in range(2,n):
			if n%p == 0:
				prime = False
		if prime:
				primes.append(n)
	print(primes)

if __name__ == "__main__":
	main(sys.argv[1:])
