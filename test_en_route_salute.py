from en_route_salute import en_route_salute as enrs

"""Test cases
==========

Inputs:
    (string) s = ">----<"
Output:
    (int) 2

Inputs:
    (string) s = "<<>><"
Output:
    (int) 4
"""

s = ">----<"
ss = "<<>><"
sss = "--->-><-><-->-"

print(enrs(s), "\n")
print(enrs(ss), "\n")
print(enrs(sss), "\n")