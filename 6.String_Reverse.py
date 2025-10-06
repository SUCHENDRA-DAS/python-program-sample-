class Reverse:
    def StringReverse(self,sentence):
        words=sentence.split( )
        words=words[::-1]
        return' '.join(words)
string=Reverse()
sentence=input("Enter A String : ")
print("The Reverse Of The String Is : ",string.StringReverse(sentence))
