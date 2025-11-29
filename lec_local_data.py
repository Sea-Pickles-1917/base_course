def changer(a: int, b: list):
    a = 3
    b[0] = 'Good'


x = 10
y = [1, 2, 4]

changer(x, y)
print(x)
print(y)

changer(x, y[:])
print(y)