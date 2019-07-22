def curve_pre():
    a = 10
    def curve(x):
        return a*x*x
    return curve

f = curve_pre()
print(f(2))


def curve_2(x, a=10):
    return x*x*a

print(curve_2(2))


