# MrJ
# 2/20/24
# Purpose: Read data from a csv file into a list
# Determine and show the statistics of the data to include:
# -Average -Maximum -Minimum -Week with highest price -Week with lowest
# How many weeks where the price was:
# -Below 1.00 -Between 1.00 and 1.05 -Between 1.05 and 1.10
# -Between 1.10 and 1.15 -Greater than 1.15
# Plot the weekly price data on a bar OR line chart
# Plot the price range data on a pie chart
# The data is the weekly price of widgets for one year (52 weeks)
# filename: weeklyPrices.csv
# I have not copied the code below from anyone or from any website.

import csv
import matplotlib.pyplot as plt

def main():
	# Call function to create list from CSV file
	prices = create_list()
	# Variables
	average = 0.0
	maximum = 0.0
	minimum = 0.0
	highest_week = 0
	lowest_week = 0
	# Range accumulators:
	# Price ranges Below 1.00
	below = 0
	# Price ranges Between 1.00 and 1.05
	between1 = 0
	# Price ranges Between 1.05 and 1.10
	between2 = 0
	# Price ranges Between 1.10 and 1.15
	between3 = 0
	# Price ranges Greater than 1.15
	greater = 0
	
	average = sum(prices) / len(prices)
	highest_week = max(prices)
	index_largest = prices.index(highest_week)
	lowest_week = min(prices)
	index_smallest = prices.index(lowest_week)
	
	# Accumulate ranges
	for price in prices:
		if price < 1.00:
			below += 1
		elif 1.00 <= price < 1.05:
			between1 += 1
		elif 1.05 <= price < 1.10:
			between2 += 1
		elif 1.10 <= price < 1.15:
			between3 += 1
		elif 1.15 <= price:
			greater += 1
		else:
			print("Error")

	
	# Print Results
	print(f"\n              Average price of widgets: {average:.3f}")
	print(f"\n               Week with highest price: week {index_largest + 1}")
	print(f"\n                         Highest price: {highest_week}")
	print(f"\n                Week with lowest price: week {index_smallest + 1}")
	print(f"\n                          Lowest price: {lowest_week}")
	# Print Ranges
	print(f"\n           Weeks with price below 1.00: {below} weeks")
	print(f"\nWeeks with price between 1.00 and 1.05: {between1} weeks")
	print(f"\nWeeks with price between 1.05 and 1.10: {between2} weeks")
	print(f"\nWeeks with price between 1.10 and 1.15: {between3} weeks")
	print(f"\n    Weeks with price greater that 1.15: {greater} weeks")
	print()
	
	# Plot weekly price data on a line chart
	create_line(prices)
	# Data to send to pie chart
	pie_chart_data = [below, between1, between2, between3, greater]
	create_pie(pie_chart_data)
	
	
def create_list():
	# Open File
	with open("weeklyPrices.csv", "r") as infile:
		# Create a CSV Reader Object
		weekReader = csv.reader(infile)
		weekly_prices = []
		# Note that weekly_prices is a list of one value lists.
		for row in weekReader:
			weekly_prices.append(row)
	
	# Converts list of Strings into list of Floats
	float_prices = []
	for price in weekly_prices:
		# Here there is only one index, but must be specified 
		# since weekly_prices is a list of lists.
		float_prices.append(float(price[0]))
	
	# Testing for float_prices
	# As it stands, float_prices is a list of individual float prices 
	# representing the weekly price of widgets for one year.
	return float_prices
	
	
def create_line(weekly_prices):
	# Set grid visibility to true
	plt.grid(visible=True)
	# Build Line Chart
	plt.plot(weekly_prices, marker=".")
	# Add a Title
	plt.title("Widget Prices for One Year", fontsize = 20)
	# Add a label to the x-axis
	plt.xlabel("Week", fontsize=14)
	# Add a label to the y-axis
	plt.ylabel("Price Per Widget", fontsize = 14)
	# Display Chart
	plt.show()
	
	
def create_pie(chart_data):
	# Create range labels
	ranges = ["< 1.00", "1.00 - 1.05", "1.05 - 1.10", "1.10 - 1.15", "> 1.15"]
	# Build Pie Chart
	plt.pie(chart_data, labels=ranges, autopct = "%.1f%%")
	
	# Add a Title
	plt.title("Widget Price Range Over 1 Year")
	
	# Display Chart
	plt.show()
		
		
main()

