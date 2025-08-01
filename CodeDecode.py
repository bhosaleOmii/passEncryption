import random
import string

while True:

    a=int(input("Enter a 1 for'coding' and 2 for 'decoding':"))

    #print(lst)


    if a== 1 :
        passs=input("Enter a password:")

        lst=passs.split()                                               #split string into list
        final_result=[]
        for words in lst:
            if len(words)>=3:
                newlst=list(words)                                      #make a list for letters in words
                popL=newlst.pop(0)                                      #pops first letter
                newlst.append(popL)                                     #append pop letter at last
                #print(newlst)
                starLetters=random.choices(string.ascii_letters,k=3)    #creates a random letters
                #newlst[:0]=starLetters
                endLetters=random.choices(string.ascii_letters,k=3)
                #newlst.extend(endLetters)
                newlst=starLetters + newlst + endLetters                #creates a new list
                #print(newlst)
                Codee=''.join(newlst)                                   #joins a letters in list
                final_result.append(Codee)                              #add the words in list final_result[]
                passCode=' '.join(final_result)                         #joins a list
                
            
            elif len(words)<=2:
                newstr=list(words)
                newstr.reverse()
                #print(newstr)
                starLetters=random.choices(string.ascii_letters,k=3)
                endLetters=random.choices(string.ascii_letters,k=3)

                newstr=starLetters + newstr + endLetters 
                #print(newstr)
                codd=''.join(newstr)
                final_result.append(codd)
                #finalstr=''.join(final_result)
                passCode=' '.join(final_result)
            
        
        print(f"Your CODED pass is >>> {passCode}")
            
    elif a == 2  :

        code=input("Enter a code for Decoding:")
        rlst=code.split()
        #print(rlst)
        Decoded=[]

        for words in rlst:
            if len(words) > 8:
                neWord=list(words)                                      #createss a list of letters in words
                del neWord[:3]                                          #delet a lists from 0 to 2 index
                del neWord[len(neWord)-3:]                              #delet a lists for last three indices
                popLetter=neWord.pop()                                  #pops last letter
                neWord.insert(0,popLetter)                              #insert a popletters at first in list neWord
                Dpass=''.join(neWord)                                   #joins a letters in list neWord
                Decoded.append(Dpass)                                   #adds words in Dpass in list Decoded 
                DecodedPass=' '.join(Decoded)                           #joins a words in Decoded list

            elif len(words) <= 8:
                newWord=list(words)
                
                del newWord[:3]
                del newWord[len(newWord)-3:]
                popLet=newWord.pop()
                newWord.insert(0,popLet)
                Dpasss=''.join(newWord)
                Decoded.append(Dpasss)
                DecodedPass=' '.join(Decoded)
        #print(DecodedPass)
        print(f"Your DECODED pass is >>> {DecodedPass}")


