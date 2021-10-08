def find_gcd(a,b):
	
	if (a == 0):
		return b
	if (b == 0):
		return a

	if (a == b):
		return a

	if (a > b):
		return find_gcd(a-b, b)
	return find_gcd(a, b-a)

a, b = map(int, input("Enter numbers for finding gcd ").split())
if(find_gcd(a, b)):
	print('GCD of', a, 'and', b, 'is', find_gcd(a, b))
else:
	print('not found')