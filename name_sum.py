# MrJ
# 1/23/24
# Purpose: Enter a list of names, type "done" when finished listing
# Print number of names entered

def main():
    name = ""
    total = 0

    # While name is not "done", ask for another name
    while name != "done":
        name = input("Enter a name, type done to stop: ")

        # If name is not done, add to total
        if name != "done":
            total += 1

    print(f"Your total number of names is {total}.")

          
main()
