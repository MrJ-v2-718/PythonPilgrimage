# An exploration of the Fibonacci sequence.

import matplotlib.pyplot as plt

def fibonacci():
	# Initialize f1 and f2
	f1 = 0
	f2 = 1
	sequence = [f1, f2]
	
	display_menu()
	iterations = int(input(("Please enter the number of iterations: ")))
	
	# Loop to generate Fibonacci numbers
	for f in range(iterations - 2):
		f3 = f1 + f2
		sequence.append(f3)
		f1 = f2
		f2 = f3
		
	print(sequence)
	create_chart(sequence)
	
	
def create_chart(sequence):
	# Set grid visibility to true
	plt.grid(visible=True)
	# Build Line Chart
	plt.plot(sequence, marker=".")
	# Add a Title
	plt.title("Fibonacci Numbers", fontsize = 20)
	# Add a label to the x-axis
	plt.xlabel("Sequence Number", fontsize=14)
	# Add a label to the y-axis
	plt.ylabel("Fibonacci Value", fontsize = 14)
	# Display Chart
	plt.show()


def display_menu():
	print()
	print(f"      Welcome to Fibonacci, an application for finding Fibonacci numbers.")
	print()
	print(f"  A Fibonacci number is a number equal to the sum of its two preceding numbers.")
	print()
	print("CAUTION: You are being prompted for a number to explore all Fibonacci numbers to.")
	print(f"   Please note that as the number increases, so do computational requirements.")
	print(f"                  Searching to 50 should be a great start!")
	print()
	
	
fibonacci()

