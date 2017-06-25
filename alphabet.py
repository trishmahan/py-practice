import sys

def AlphabetSoup(str):
	chars = list(str)
	sortedChars = sorted(chars)
	return "".join(sortedChars)

print AlphabetSoup(sys.argv[1])