from sys import stdin
from sys import maxsize as MAX_VALUE



def countMinStepsToOne(n) :
	if n == 1 :
		return 0

	minSteps = [0] * (n + 1)
	
	minSteps[1] = 0

	for currStep in range(2, (n + 1)) :

		subtractOne = MAX_VALUE
		divideByTwo = MAX_VALUE
		divideByThree = MAX_VALUE

		subtractOne = minSteps[currStep - 1]

		if currStep % 2 == 0 :
			divideByTwo = minSteps[currStep // 2]

		if currStep % 3 == 0 :
			divideByThree = minSteps[currStep // 3]

		minSteps[currStep] = 1 + min(subtractOne, divideByTwo, divideByThree)

	return minSteps[n]



#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))