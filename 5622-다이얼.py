import math

s = list(map(lambda x : math.ceil((ord(x) - 64)/3) + 2 if x <= "R" else math.ceil((ord(x) - 65)/3) + 2, input()))
for i, v in enumerate(s):
    if v == 11 : s[i] = 10

print(sum(s))