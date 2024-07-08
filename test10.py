'''x = 10000
def d(y):
    global x
    x *=2
    x += y
    return x
def b(y):
    x = 20000
    x *= 3
    x += y
    return x

print(d(1000))'''

'''x = 5
def f1(y):
    y = x + 1
    print(y)
    return y
def f2():
    x = 10
    x = x + f1(x)
    return x
x = f2()
print(x)'''

'''def add(a, b):
    a = 7
    return a + b
i = 5; j = 6
print(add(i, j))'''

def F(x, y = 5, z =10):
    x += 1
    y += 1
    z += 1
    return x + y +z
x = F(10,20,30)
print(x)




