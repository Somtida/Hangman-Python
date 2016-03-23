import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    check=True
    for i in secretWord:
        if i in lettersGuessed:
            check = check and True
        else: check = check and False
    return check




def getGuessedWord(secretWord, lettersGuessed):
    secret=''
    
    for i in range(len(secretWord)):
        secret += "_ "
    for j in lettersGuessed:
        if secretWord.find(j)!=-1:
            dupli=secretWord.count(j)
            if dupli==2:
                index=secretWord.find(j)
                index2=secretWord.find(j,index+1)
                secret=secret[:(index*2)]+j+secret[((index*2)+1):]
                secret=secret[:(index2*2)]+j+secret[((index2*2)+1):]
            elif dupli==3:
                index=secretWord.find(j)
                index2=secretWord.find(j,index+1)
                index3=secretWord.find(j,index2+1)
                secret=secret[:(index*2)]+j+secret[((index*2)+1):]
                secret=secret[:(index2*2)]+j+secret[((index2*2)+1):]
                secret=secret[:(index3*2)]+j+secret[((index3*2)+1):]
            else:
                index=secretWord.find(j)
                secret=secret[:(index*2)]+j+secret[((index*2)+1):]
    secret=secret.replace(' ','')
    secret=secret.replace('_','_ ')       
    return secret



def getAvailableLetters(lettersGuessed):
    str = string.ascii_lowercase
    for i in lettersGuessed:
        if i in str:
            str=str.replace(i,'')
    return str
    

def hangman(secretWord):
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
    
    mistakesMade=8
    guessedList=[]
    guessed=[]
    #lettersGuessed='1'
    
    while mistakesMade>=0:
        if mistakesMade==0:
            print "-----------"
            print "Sorry, you ran out of guesses. The word was "+secretWord+"."
            break
        print "-------------"
        print "You have "+str(mistakesMade)+" guesses left."
        print "Available letters: "+getAvailableLetters(guessedList)
        lettersGuessed=raw_input("Please guess a letter:  ")
        lettersGuessed=lettersGuessed.lower()
        guessedList.append(lettersGuessed)
        if isWordGuessed(secretWord, guessedList)==False:
            if lettersGuessed not in secretWord:
                
                if lettersGuessed in guessed:
                    print "Oops! You've already guessed that letter: ",
                else:
                    mistakesMade-=1
                    print "Oops! That letter is not in my word: ",
                guessed.append(lettersGuessed)
                print getGuessedWord(secretWord, guessedList)
            else: 
                if lettersGuessed in guessed:
                    print "Oops! You've already guessed that letter: ",
                else:
                    print "Good guess: ",
                guessed.append(lettersGuessed)
                print getGuessedWord(secretWord, guessedList)
        
                
        elif isWordGuessed(secretWord, guessedList)==True:
                 guessed.append(lettersGuessed)
                 print "Good guess: "+getGuessedWord(secretWord, guessedList)
                 print "-----------"
                 print "Congratulations, you won!"
                 break 
        


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)