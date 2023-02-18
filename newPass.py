#!/bin/python3
'''
    @author:     Jose Luis Núñez
    
    @copyright:  Creative Commons CC BY-NC-SA ipserc 2023
    
    @license:    GNU General Public License v3.0
    
    @contact:    jlncpub@selenitas.es
    
    @deffield    created: 2023/02/18
				 updated: See UPDATED at Program Facts
    
    @version:	See VERSION at Program Facts
   '''
# #################################################
# Programa para generar passwords seguras
# 
# #################################################

from random import randint, seed, sample, shuffle
from math import factorial
from itertools import permutations
from os.path import basename

# Program Facts
PROGRAM = basename(__file__)
VERSION = "1.0.0 (2023_0218_2359)"
UPDATED = "2023/02/18"
CREATED = "2023/02/18"
AUTHOR = "Jose Luis Núñez Crespi"
LICENSE = "GNU General Public License v3.0"
EMAIL = "jlncpub@selenitas.es"

# maximum number of iterations to generate the desired password
MAXITER = 500 

# The sets of characters
MAYS = "QWERTYUIOPASDFGHJKLZXCVBNM"
MINS = "mnbvcxzpoiuytrewqlkjhgfdsa"
SYMB = "@!#€$%&/(){}=+-*[]·"
NMBR = "1357902468"

# The Ids of the sets of characters
idNOSET = 0
idFIRST = 1
idMAYS = 1
idMINS = 2
idNMBR = 3
idSYMB = 4	# MUST BE THE LAST
idLAST = 4

# Counters to track the amount of characters used
maysCount = 0
minsCount = 0
nmbrCount = 0
symbCount = 0

# Rules with the minimum nomber of characters of a set to use for the password 
maysRuleCount = 0
minsRuleCount = 0
nmbrRuleCount = 0
symbRuleCount = 0

def progamFacts():
	print(	"PROGRAM..: " + PROGRAM + "\n" + \
			"VERSION..: " + VERSION + "\n" + \
			"UPDATED..: " + UPDATED + "\n" + \
			"CREATED..: " + CREATED + "\n" + \
			"AUTHOR...: " + AUTHOR + "\n" + \
			"LICENSE..: " + LICENSE + "\n" + \
			"EMAIL....: " + EMAIL + "\n")


def shuffle(string):
	return ''.join(sample(string,len(string)))

def Permute(string):
	if len(string) > 8:
		print("Are you sure that you want to do it? It will generate %g permutations" % factorial(len(string)))
		ans = input("Enter Y to proceed:")
		if ans != "Y":
			return []
	return [''.join(p) for p in permutations(string)]
 
def printPermuteList(string):
	print('\n'.join(Permute(string)))

def resetCounters():
	global maysCount
	global minsCount
	global nmbrCount
	global symbCount

	maysCount = 0
	minsCount = 0
	nmbrCount = 0
	symbCount = 0
	
def matchRules(allowedCharsSet):
	maysCheck = not idMAYS in allowedCharsSet
	minsCheck = not idMINS in allowedCharsSet
	nmbrCheck = not idNMBR in allowedCharsSet
	symbCheck = not idSYMB in allowedCharsSet
	return (maysCount >= maysRuleCount or maysCheck) and \
	(minsCount >= minsRuleCount or minsCheck) and \
	(nmbrCount >= nmbrRuleCount or nmbrCheck) and \
	(symbCount == symbRuleCount or symbCheck)

def getCharSet(Set):
	idx = randint(0,len(Set)-1)
	return Set[idx:idx+1]

def selectCharSet(allowedCharsSet, idLAST):
	idSet = idNOSET
	while not (idSet in allowedCharsSet):
		idSet = randint(idFIRST, idLAST)
	return idSet

def onlySYMB(allowedCharsSet):
	return allowedCharsSet == {idSYMB}
	
def genratePass(lenPass, allowedCharsSet):
	global maysCount
	global minsCount
	global nmbrCount
	global symbCount

	seed()
	
	passCreated = False
	while not passCreated:
		newPass = ""
		hasMAYS = not idMAYS in allowedCharsSet 
		hasMINS = not idMINS in allowedCharsSet
		hasNMBR = not idNMBR in allowedCharsSet 
		hasSYMB = not idSYMB in allowedCharsSet
		resetCounters()

		for iter in range(0, lenPass):
			# select a Set of characters
			idSet = selectCharSet(allowedCharsSet, idSYMB)
			if idSet == idMAYS:
				newPass = newPass + getCharSet(MAYS)
				maysCount += 1
				hasMAYS = True
			elif idSet == idMINS:
				newPass = newPass + getCharSet(MINS)
				minsCount += 1
				hasMINS = True
			elif idSet == idNMBR:
				newPass = newPass + getCharSet(NMBR)
				nmbrCount += 1
				hasNMBR = True
			elif idSet == idSYMB:
				hasSYMB = True
				symbCount += 1
				if (symbCount > symbRuleCount) and not onlySYMB(allowedCharsSet):
					idSet = selectCharSet(allowedCharsSet, idNMBR)
					if idSet == idMAYS:
						newPass = newPass + getCharSet(MAYS)
						maysCount += 1
						hasMAYS = True
					elif idSet == idMINS:
						newPass = newPass + getCharSet(MINS)
						minsCount += 1
						hasMINS = True
					elif idSet == idNMBR:
						newPass = newPass + getCharSet(NMBR)
						nmbrCount += 1
						hasNMBR = True
				else:
					newPass = newPass + getCharSet(SYMB)

		passCreated = hasMAYS and hasMINS and hasNMBR and hasSYMB
	return newPass

# #################################################
# Programa principal
# #################################################
if __name__ == "__main__":
	progamFacts()
	# Password Length
	lenPass = 16
	
	# Allowed Chars Set
	allowedCharsSet = {idMAYS, idMINS, idNMBR, idSYMB}
	
	# Rules as the minmum number of characters of a set in the password
	# for SYMB set this number is exact, if there is another set is available
	maysRuleCount = 3
	minsRuleCount = 3
	nmbrRuleCount = 3
	symbRuleCount = 2
	
	# Shuffle the sets of characters
	MAYS = shuffle(MAYS)
	MINS = shuffle(MINS)
	NMBR = shuffle(NMBR)
	SYMB = shuffle(SYMB)
	
	# ready to do the stuff
	iteration = 0
	while not matchRules(allowedCharsSet):
		iteration += 1 
		newPass = genratePass(lenPass, allowedCharsSet)
		if (iteration > MAXITER):
			break
	
	# Print results
	if (iteration > MAXITER):
		print("WARNING: The password may not comply with all the rules")
		
	if (iteration > 1):
		s = "s"
	else:
		s = ""
	print("Password generated in " + str(iteration) + " iteration" + s)
	print("> > > > > > This is your 1st new password: " + newPass)
	print("> > > > > > This is your 2nd new password: " + shuffle(newPass))

	# ---- printPermuteList(newPass)
