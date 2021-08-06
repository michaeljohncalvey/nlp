import numpy as np

X = "INTENTION"
Y = "EXECUTION"

D = [[0 for x in range(len(X)+1)] for y in range(len(Y)+1)] 

for char in range(len(X)+1):
	D[char][0] = char

for char in range(len(Y)+1):
	D[0][char] = char

print("Initialized starting matrix")

for i in range(1, len(X)+1):
	for j in range(1, len(Y)+1):

		D[i][j] = min(
			D[i-1][j] + 1,
			D[i][j-1] + 1,
			D[i-1][j-1] + 2 if X[i-1] is not Y[j-1] else D[i-1][j-1]
			)

print(np.array(D))
