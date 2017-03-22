import random
print "This game is called cows and bulls. "
numbers = [1,2,3,4,5,6,7,8,9,0]
answelist = random.sample(numbers,4)
answer = ""
for x in answelist:
	answer = answer + str(x)
numguesses = 0
while True:
	cow = 0
	bulls = 0
	guess = raw_input("Take a guess at the number: ")
	if len(guess) != 4:
		print "Lets try that again. A FOUR digit number."
	else:
		for chars in answer:
			if chars in guess:
				bulls+=1
		
		for x in range(4):
			if answer[x] == guess [x]:
				cow += 1
	bulls = bulls - cow	
	numguesses += 1
	print cow, "cows",bulls, "bulls"			
	if cow >= 4:
		print "You got it!"
		print "You took " + str(numguesses) + " guesses."
		break
