def factorial (n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

	
answer = factorial (10)
print (answer)

str (answer)

from collections import Counter
answer = '3628800'
print(Counter(list(answer))['0'])
