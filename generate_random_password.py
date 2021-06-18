# Auhor: Karthik Kumar Hiraskar

# Command line arguments:
#      1st Arg: [Optional] number of Random passwords to generate
#      2nd Arg: [Optional] password length

import random, string
import os, sys

passwordLength=12
possibleChars=string.ascii_letters+string.digits+string.punctuation
num=1

argLen=len(sys.argv)
if argLen>1: num=int(sys.argv[1])
if argLen>2: passwordLength=int(sys.argv[2])

def printPossibleChars():
    print(possibleChars)
def getOneRandomPass():
   return ''.join(random.choice(possibleChars) for i in range(passwordLength))

for i in range(num):   
   print(getOneRandomPass())

