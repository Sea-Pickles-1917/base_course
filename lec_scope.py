x0 = 10


def move(t):
    x = x0 * t
    return x


print(move(3))

a = 'Good'


def test_local_data():
    a = 'Bad'
    print(a, id(a))


test_local_data()
print(a, id(a))