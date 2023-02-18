#!/bin/python3
# #################################################
# Programa para generar passwords seguras
# 
# #################################################

from random import randint, seed, sample, shuffle
from math import factorial
from itertools import permutations

MAYS = "QWERTYUIOPASDFGHJKLZXCVBNM"
MINS = "mnbvcxzpoiuytrewqlkjhgfdsa"
SYMB = "@!#€$%&/(){}=+-*[]"
NMBR = "1357902468"

idFirst = 1
idMAYS = 1
idMINS = 2
idNMBR = 3
idSYMB = 4	# MUST BE THE LAST
idLast = 4

maysCount = 0
minsCount = 0
nmbrCount = 0
symbCount = 0

maysRuleCount = 0
minsRuleCount = 0
nmbrRuleCount = 0
symbRuleCount = 0

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
	
def matchConditions(allowedCharsGroups):
	maysCheck = not idMAYS in allowedCharsGroups
	minsCheck = not idMINS in allowedCharsGroups
	nmbrCheck = not idNMBR in allowedCharsGroups
	symbCheck = not idSYMB in allowedCharsGroups
	return (maysCount >= maysRuleCount or maysCheck) and \
	(minsCount >= minsRuleCount or minsCheck) and \
	(nmbrCount >= nmbrRuleCount or nmbrCheck) and \
	(symbCount == symbRuleCount or symbCheck)

def getSet(group):
	idx = randint(0,len(group)-1)
	return group[idx:idx+1]

def selectCharGroup(allowedCharsGroups, idLast):
	idGroup = -1
	while not (idGroup in allowedCharsGroups):
		idGroup = randint(idFirst, idLast)
	return idGroup

def onlySYMB(allowedCharsGroups):
	return allowedCharsGroups == {idSYMB}
	
def genratePass(lenPass, allowedCharsGroups):
	global maysCount
	global minsCount
	global nmbrCount
	global symbCount

	seed()
	
	passCreated = False
	while not passCreated:
		newPass = ""
		hasMAYS = not idMAYS in allowedCharsGroups 
		hasMINS = not idMINS in allowedCharsGroups
		hasNMBR = not idNMBR in allowedCharsGroups 
		hasSYMB = not idSYMB in allowedCharsGroups
		resetCounters()

		for iter in range(0, lenPass):
			# select a group of characters
			#idGroup = randint(idMAYS, idSYMB)
			idGroup = selectCharGroup(allowedCharsGroups, idSYMB)
			if idGroup == idMAYS:
				newPass = newPass + getSet(MAYS)
				maysCount += 1
				hasMAYS = True
			elif idGroup == idMINS:
				newPass = newPass + getSet(MINS)
				minsCount += 1
				hasMINS = True
			elif idGroup == idNMBR:
				newPass = newPass + getSet(NMBR)
				nmbrCount += 1
				hasNMBR = True
			elif idGroup == idSYMB:
				hasSYMB = True
				symbCount += 1
				if (symbCount > symbRuleCount) and not onlySYMB(allowedCharsGroups):
					#idGroup =  randint(idMAYS, idNMBR)
					idGroup = selectCharGroup(allowedCharsGroups, idNMBR)
					if idGroup == idMAYS:
						newPass = newPass + getSet(MAYS)
						maysCount += 1
						hasMAYS = True
					elif idGroup == idMINS:
						newPass = newPass + getSet(MINS)
						minsCount += 1
						hasMINS = True
					elif idGroup == idNMBR:
						newPass = newPass + getSet(NMBR)
						nmbrCount += 1
						hasNMBR = True
				else:
					newPass = newPass + getSet(SYMB)

		passCreated = hasMAYS and hasMINS and hasNMBR and hasSYMB
	return newPass

# #################################################
# Programa principal
# #################################################
if __name__ == "__main__":
	
	# Password Length
	lenPass = 16
	
	# Allowed Chars Set
	allowedCharsGroups = {idMAYS, idMINS, idNMBR, idSYMB}
	
	# Pass Conditions
	maysRuleCount = 3
	minsRuleCount = 3
	nmbrRuleCount = 3
	symbRuleCount = 2
	
	iteration = 0
	while not matchConditions(allowedCharsGroups):
		iteration += 1 
		newPass = genratePass(lenPass, allowedCharsGroups)
		if (iteration > 500):
			break
	
	print("Password generated in " + str(iteration) + " iterations")
	print("> > > > > > This is your new password: " + newPass)
	print("> > > > > > This is your new password: " + ''.join(sample(newPass,len(newPass))))

	# --- printPermuteList(newPass)
