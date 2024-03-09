# append demo
# Purpose: Get User Input for 2 new comicChars, add to file

def main():
    # Get two character names
    char1 = input("Character 1: ")
    char2 = input("Character 2: ")

    # open the file
    with open("comicChar.txt","a") as mai_file:
        # write names to file
        mai_file.write(char1 + "\n")
        mai_file.write(char2 + "\n")

main()
