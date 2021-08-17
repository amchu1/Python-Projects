def anagram(str1,str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    if len(str1) != len(str2):
        return False
    dictionary = {}
    for char in str1:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    for char in str2:
        if char in dictionary:
            dictionary[char] -= 1
        else:
            dictionary[char] = 1
    for key in dictionary:
        if dictionary[key] != 0:
            return False
    return True

x = anagram("Clint Eastwood","old WEST action")
print(x)