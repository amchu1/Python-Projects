import string

def is_pangram(s):
    seen = []
    const = list('abcdefghijklmnopqrstuvwxyz')
    testStr = ''.join(filter(str.isalpha, s)).lower()
    for char in testStr:
        if char not in seen:
            seen.append(char)

    if sorted(seen) == const:
        return True
    else:
        return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
