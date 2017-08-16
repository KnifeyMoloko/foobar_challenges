import re
import string


def answer(s):
    # your code here
    letters = string.lowercase
    mirror = letters[::-1]
    new = ""

    for char in s:
        if char in letters:
            index_in_s = letters.find(char)
            #s = s.replace(char, mirror[index_in_s])
            #s = re.sub(char, mirror[index_in_s], s)
            #print char, " ", mirror[index_in_s]
            new = new + mirror[index_in_s]
        else:
            new = new + char
    return new