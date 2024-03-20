class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    # TODO: Define get_win_percentage()
    # For the instance method get_win_percentage(), the formula is:
    # wins / (wins + losses). Note: Use floating-point division.
    def get_win_percentage(self):
        win_percentage = self.wins / (self.wins + self.losses)
        return win_percentage
    
    # TODO: Define print_standing()
    # For instance method print_standing(), output the win percentage of the team with two 
    # digits after the decimal point and whether the team has a winning or losing average. 
    # A team has a winning average if the win percentage is 0.5 or greater.
    def print_standing(self):
        win_percentage = self.get_win_percentage()
        print(f"Win percentage: {win_percentage:.2f}")
        
        if win_percentage >= 0.5:
            print(f"Congratulations, Team {self.name} has a winning average!")
        elif win_percentage < 0.5:
            print(f"Team {self.name} has a losing average.")
        else:
            print("Error.")


if __name__ == "__main__":
    team = Team()
   
    user_name = input("Enter team name: ")
    user_wins = int(input("Enter wins: "))
    user_losses = int(input("Enter losses: "))
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()
