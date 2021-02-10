# wc.py
# wc in python. Prints number of lines, words, and
# characters in a file

def main():
    infileName = input("Please enter a file name. ")


    # Get line count
    infile = open(infileName, "r")
    x = len(infile.readlines())


    # Get word count
    infile = open(infileName, "r")
    y = len(infile.read().split())


    # Get character count
    infile = open(infileName, "r")
    z = len(infile.read()) 

    # Print output

    print(x, y, z, infileName)

main()
