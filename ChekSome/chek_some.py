# A simple, command line, check sum tool.

def check_sum():
	print()
	print("Welcome to ChekSome, a simple checksum tool.")
	print()
	check_sum1 = input(f" Enter the first checksum: ").lower()
	check_sum2 = input(f"Enter the second checksum: ").lower()
	
	if check_sum1 == check_sum2:
		print()
		print(check_sum1)
		print(check_sum2)
		print()
		print("Checksums Match")
	elif check_sum1 != check_sum2:
		print()
		print(check_sum1)
		print(check_sum2)
		print()
		print("Checksum Mismatch")
	else:
		print()
		print("Error")
		
check_sum()

