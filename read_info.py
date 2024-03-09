# Read Demo
# Purpose: read info from comicChar.txt

def main():
    # call function to read data
    characters = readData()

    print(characters)

def readData():
    with open("comicChar.txt","r") as infile:

        character_list = infile.read()
        
    return character_list

main()
