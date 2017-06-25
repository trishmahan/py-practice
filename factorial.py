import sys

x = sys.argv[0]

def FirstFactorial(num):
	total = 1
	for i in range(1, num + 1):
		total = i * total
	return total

print FirstFactorial(int(sys.argv[1]))