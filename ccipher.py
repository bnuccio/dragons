# ccipher.py
# Making the ceaser cipher in python


def main():

    qstString = input("Enter the word to be encrypted followed by the key (1-9). ")
    print()

    word, key = qstString.split()
    key = int(key)


    if key > 9:
        print("Number must be between 1 and 9!!!!")
        quit()


    msg = ""
    for ch in word:
        msg = msg + chr(ord(ch) + key)

    
    print(msg)
    print()



    answer = input("Enter the word to be decrypted ")

    msg = ""
    for ch in answer:
        msg = msg + chr(ord(ch) - key)


    print(msg)
    


main()
