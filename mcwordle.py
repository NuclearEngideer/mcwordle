from time import time
import random

guess = []
answer='piton'

allowedWords=['crate','atoms','adieu','piton', 'moose', 'train', 'noble','crazy']

letters={'1': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
         '2': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
         '3': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
         '4': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
         '5': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']}

def checkWord(guess, answer):
  res=[0,0,0,0,0]
  indeces=[]
  i=0
  g=-1
  while i<5:
    # If guess is in word, record location(s)
    if guess[i] in answer:
      g = answer.index(guess[i])
    # Remove letters from the guess set if they're not in the word at all
    else:
      letters['1'].pop(letters['1'].index(guess[i]))
      letters['2'].pop(letters['2'].index(guess[i]))
      letters['3'].pop(letters['3'].index(guess[i]))
      letters['4'].pop(letters['4'].index(guess[i]))
      letters['5'].pop(letters['5'].index(guess[i]))
    # Figure out if any letters are in the proper position, or are in the word and in the wrong place
    indeces=getIndexes(guess[i], answer)
    # First set yellows:
    if g in (indeces):
      res[i]=1
    # Set Greens
    if g==i:
      res[i]=2
    i=i+1
  return res

def getIndexes(guessed_letter,answer):
  return [i for i, x in enumerate(answer) if x == guessed_letter]

def popYellows(guess,res):
  i=1
  while i<6:
    if res[i-1] == 1:
      letters[str(i)].pop(letters[str(i)].index(guess[i]))
    i+=1

def rollLetter(letterset):
  return letterset[random.randrange(0,len(letterset))]

guess=list('crate')
guesscount=1
result=checkWord(guess, answer)
print(result)
while result != [2,2,2,2,2]:
  i=0
  for i in range(1,6):
    if result[i-1] == 1 or result[i-1] == 0:
      guess[i-1] = rollLetter(letters[str(i)])
  result = checkWord(guess,answer)
  print(result)
  
print('wait')
# def cleanLetters(guess[i])