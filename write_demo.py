# Write Demo
# Purpose: Create a file and add two lines of information

def main():
    # open file named comicChar.txt
    outfile = open("comicChar.txt","w")

    # Write names to file
    outfile.write("Batman\n")
    outfile.write("Joker\n")

    # close file
    outfile.close()

main()
