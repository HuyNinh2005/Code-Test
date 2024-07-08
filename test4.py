import math
n = int(input())

sc = 0
for i in range(n + 1):
    sc = math.sqrt(sc + 3)

sd = 0
tich = 1
for i in range(1, n + 1):
    tich = tich * i
    sd = sd + tich

print(f"{sc:.3f}")
print(f"{sd:.3f}")