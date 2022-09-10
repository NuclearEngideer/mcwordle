from time import time
import random
import json
import numpy as np
from colorama import Back, Style

num_guesses=np.array([])

words=open('data.json')
fiveletterwords=json.load(words)
solutions=fiveletterwords['solutions']
allowedWords=fiveletterwords['valid_words']

def checkWord(guess, answer, letters):
  res=[0,0,0,0,0]
  i=0
  g=[]
  while i<5:
    indeces=[]
    # If guess is in word, record location(s)
    if guess[i] in answer:
      indeces=getIndexes(guess[i], answer)
      for index in indeces:
        # First set yellows:
        if res[i] != 2:
          res[i]=1
        if i==index:
          res[i]=2
    # Remove letters from the guess set if they're not in the word at all
    else:
      indeces=[-1]
      for j in range(1,6):
        if guess[i] in letters[str(j)]:
          letters[str(j)].pop(letters[str(j)].index(guess[i]))

    i=i+1
  return res

def getIndexes(guessed_letter,answer):
  return [i for i, x in enumerate(answer) if x == guessed_letter]

def popYellows(guess,res,yellow_letters,letters):
  i=1
  while i<6:
    if res[i-1] == 1:
      letters[str(i)].pop(letters[str(i)].index(guess[i-1]))
      yellow_letters.append(guess[i-1])
    i+=1
  return yellow_letters

def rollLetter(letterset):
  return letterset[random.randrange(0,len(letterset))]

def newWord(guess, result, letters):
  for i in range(1,6):
    if result[i-1] == 1 or result[i-1] == 0:
      guess[i-1] = rollLetter(letters[str(i)])
  return guess

def printRes(guess, result):
  # let's color the letters!
  for i in range(0,5):
    if result[i]==1:
      print(Back.YELLOW + guess[i], end='')
    elif result[i]==2:
      print(Back.GREEN + guess[i], end='')
    else:
      print(Back.BLACK + guess[i], end='')
  print(Style.RESET_ALL)

def main(seed, answer):
  guess=seed
  letters={'1': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
           '2': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
           '3': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
           '4': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
           '5': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']}
  guesscount=1
  yellow_letters=[]
  result=checkWord(guess, answer, letters)
  printRes(guess, result)
  yellow_letters=popYellows(guess, result, yellow_letters, letters)
  while result != [2,2,2,2,2]:
    guess=newWord(guess, result, letters)
    while ''.join(guess) not in allowedWords and ''.join(guess) not in solutions:
      guess=newWord(guess, result, letters)
      while len(set(yellow_letters)-set(guess)) > 0:
        guess=newWord(guess,result,letters)
    result = checkWord(guess, answer, letters)
    yellow_letters=popYellows(guess, result,yellow_letters,letters)
    printRes(guess, result)
    guesscount+=1
  print(str(guesscount)+'/6')
  return guesscount

for ans in solutions[0:99]:
  num_guesses=np.append(num_guesses, main(list('crate'), ans))

print(f'\n----STATISTICS----\n'
      f'Max={num_guesses.max()}\n'
      f'Min={num_guesses.min()}\n'
      f'Avg={np.average(num_guesses)}\n'
      f'std={np.std(num_guesses)}\n')