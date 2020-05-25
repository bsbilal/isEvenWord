

def isEvenWord(oldWord):
    if len(oldWord)<1:
        return True
    newchar=oldWord[0]
    lettercount=oldWord.count(newchar)
    if lettercount%2!=0:
        return False
    else:
        oldWord=oldWord.translate({ord(newchar): None})
        if oldWord!="":
            return True
        isEvenWord(oldWord)

text = input('Enter your word for check:')
text=text.upper()
text=str(text)

if isEvenWord(text):    
    print(text,'is even word.')        
else:
    print(text,' is not an even word')