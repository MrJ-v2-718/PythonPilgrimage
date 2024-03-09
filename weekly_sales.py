# MrJ
# 2/6/2024
# Purpose: Get sales for the week, calculate average, total, max, and min

import matplotlib.pyplot as plot

def main():
	# Variables
	total_sales = 0.0
	
	daily_sales = [0.0] * 7
	days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
				    "Friday", "Saturday"]
	
	for i in range(7):
		daily_sales[i] = float(input("Enter the sales for " + days_of_week[i] + ":"))
		
	total_sales = sum(daily_sales)
	avg_sales = total_sales / len(daily_sales)
	large_sales = max(daily_sales)
	index_large = daily_sales.index(large_sales)
	small_sales = min(daily_sales)
	index_small = daily_sales.index(small_sales)
	
	# Print Results
	print(f"\nTotal sales for the week: ${total_sales:.2f}")
	print(f"\nAverage sales for the week: ${avg_sales:.2f}")
	print(f"\nBest day of the week: {days_of_week[index_large]}")
	print(f"\nWorst day of the week: {days_of_week[index_small]}")
	
	create_chart(daily_sales, days_of_week)
	
def create_chart(sales, days):
	# Specify Colors
	slice_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
	# Wedge Slice Properties
	wp = {"linewidth":1, "edgecolor":"black"}
	# Build Pie Chart
	plot.pie(sales, labels = days, colors = slice_colors, wedgeprops = wp, autopct = "%.1f%%")
	
	# Add a Title
	plot.title("Sales for the Week")
	
	# Display Chart
	plot.show()

# Call to Main
main()

