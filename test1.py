import math

a = int(input())
b = int(input())
c = int(input())

delta = b * b - 4 * a * c
if(a != 0):
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b/2*a
        print(f"Phương trình có nghiệm kép x1 = x2 = {x:.3f}")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"Phương trình có hai nghiệm: x1 = {x1:.3f} và x2 = {x2:.3f}")
else:
    if b == 0:
        print("Phương trình vô nghiệm")
    else:
        x = -c/b
        print(f"Phương trình có một nghiệm: x = {x:.3f}")

    
