a = int(input())
b = int(input())
c = int(input())
d = int(input())
bcnn = 0
for i in range(1, a * b * c * d + 1):
    if i % a == 0 and i % b == 0 and i % c == 0 and i % d == 0:
        bcnn = i
        break
print(bcnn)

