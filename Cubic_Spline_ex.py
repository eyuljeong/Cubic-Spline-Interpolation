# 삼차방정식

condition = [[0,0], [1,1], 0, 0] # y = x^3

def cubic_equation(condition):
    a = condition[0][0]
    b = condition[0][1]
    c = condition[1][0]
    d = condition[1][1]
    e = condition[2]
    f = condition[3]

    p = f*(a-c)**2 - 2*e*(a-c) + 2*(b-d) / 2*(a-c)**3
    q = f/2 - 3*a*p
    r = e - 3*a**2*p - 2*a*q
    s = b - p*a**3 - q*a**2 - r*a

    return [p, q, r, s]