password = "feheeehk"

def passwordCheckVowels(password):
    countVowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in password:
        if any(x in char for x in vowels):
            countVowels+=1
    if countVowels >= 3:
        return 'true'
    else:
        return 'false'

def passwordCheckDoubles(password):
    i = 0
    for char in password:
        if char == password[i+1]:
            return 'true'
        else:
            if i == len(password) - 2:
                return 'false'
            else:    
                i+=1
    return 'false'

def passwordCheckStrings(password):
    if 'ab' in password:
        return 'false'
    if 'cd' in password:
        return 'false'
    if 'pq' in password:
        return 'false'
    if 'xy' in password:
        return 'false'
    else:
        return 'true'

for ()
print(passwordCheckVowels(password))
