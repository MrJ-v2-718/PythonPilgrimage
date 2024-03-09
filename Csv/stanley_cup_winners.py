# MrJ
# 2/6/24
# Purpose: Ask users to chose a team, display amount of times they win
# 1990-2021

import csv

def main():
	# Open File
	with open("stanleyCupWinners3.csv", "r") as infile:
		# Create a CSV Reader Object
		winnerReader = csv.reader(infile, delimiter=",")
		
		for row in winnerReader:
			year = int(row[0])
			if year >= 1990:
				print(row[0], row[1])
				
	with open("stanleyCupWinners3.csv", "r") as infile:
		# Create a CSV Reader Object
		winnerReader = csv.reader(infile, delimiter=",")
		
		print()
		wins = 0
		
		# Ask User What Team
		team = input("Which team? ")
		
		for row in winnerReader:
			if team == row[1]:
				wins += 1
				
		print(f"{team} won {wins} times.")
		
		
main()

