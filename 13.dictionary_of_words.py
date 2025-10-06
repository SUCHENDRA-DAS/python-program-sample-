def addword():
    word=input("Enter a word : ")
    meaning=input("enter the meaning : ")
    dictionary[word]=meaning
    print("New Word Added ")
def meaning():
    checkword=input("Enter the word to find out : ")
    if checkword in dictionary:
        print("Meaning: ",dictionary[checkword])
    else:
        print("Word not found alert!!!")
def mydict():
    print(dictionary)
dictionary={}
menu="""***** Dictionary *****
choice--1 : Add a Word in Dictionary
choice--2 : Show me the meaning
choice--3 : Explore Dictionary
choice--4 : Exit"""
while True:
    print(menu)
    choice=int(input("enter your choice : "))
    if choice==1:
        addword()
    elif choice==2:
        meaning()
    elif choice==3:
        mydict()
    elif choice==4:
        print("Good Bye please visit again!!!")
        break
    else:
        print("##### invalid input ######")
