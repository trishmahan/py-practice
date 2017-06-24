def passwordCheckVowels(password):
    countVowels = 0
    for char in password:
        if char == 'a' or char == 'e' or char == 'o' or char == 'i' or char == 'u':
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
