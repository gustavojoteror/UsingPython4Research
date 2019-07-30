def intersect(s1,s2):
    res=[]
    for x in s1:
        if x in s2:
            res.append(x)
    return res

def password(lenght):
    pw = str()
    characters= 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '!@#$%^&*()_+' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in range(lenght):
        pw = pw + random.choice(characters)
    return pw



import random

L1 = [1,2,3,4,5]
L2 = [3,4,5,6,7]

Lint = intersect(L1,L2)

print(Lint)

# randomizer
print(random.choice(L1))
print(random.choice('abcdefg'))
print(password(6))

