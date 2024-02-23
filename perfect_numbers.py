# Inspiration: Number Theory by George E. Andrews
# Combinatorial and Computational Number Theory
# Page 46, Figure 3-6 "A flow diagram for a program for finding perfect numbers."

def perfect_numbers():
	n = 2
	m = 1
	s = 0
	
	print()
	print("Welcome to Perfect Numbers, an application for finding perfect numbers.")
	print()
	print("A perfect number is a number equal to the sum of its proper divisors.")
	print()
	print("Proper divisors in this context refers to all divisors except the number itself.")
	print()
	print("CAUTION: You are being prompted for a number to explore all perfect numbers to.")
	print("Please note that as the number increases, so do computational requirements.")
	print("Searching to 500 should be a great start!")
	print()
	iterations = int(input("Please enter the number you would like to search to: "))
	
	while n <= iterations:
		
		if (n / m) % 1 == 0:
			s += m
		m += 1
			
		if m > n / 2:

			if n == s:
				# Perfect Number
				print()
				print(f"{n} is a perfect number.")	
			n += 1	
			
			if n <= iterations:
				# Re-initialization of m and s with iteration loop re-start
				m = 1
				s = 0
				continue
		else:
			continue
			
		
perfect_numbers()

