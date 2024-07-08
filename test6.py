x = float(input())
y = float(input())
z = float(input())

f1 = x**2 + x * y + y**2 - 2*x - y
print(f"{f1:.2f}")

if y == 0 or y**x == 0:
    print("N/A")
else:
    f2 = (x * y * z) + (x/(y ** z))
print(f"{f2:.2f}")
