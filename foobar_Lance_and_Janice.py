import re
import string


def answer(s):
    # your code here
    letters = string.lowercase
    mirror = letters[::-1]

    def sub(matchobj):
        i = letters.find(matchobj.group(0))
        n = mirror[i]
        return n

    s = re.sub('[a-z]', sub, s)

    return s