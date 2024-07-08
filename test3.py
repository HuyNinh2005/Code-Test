a = int(input())
b = int(input())
c = int(input())
d = int(input())

maxNumber = a
if maxNumber < b:
    maxNumber = b
if maxNumber < c:
    maxNumber = c
if maxNumber < d:
    maxNumber = d

minNumber = a
if minNumber > b:
    minNumber = b
if minNumber > c:
    minNumber = c
if minNumber > d:
    minNumber = d

print(minNumber)
print(maxNumber)

