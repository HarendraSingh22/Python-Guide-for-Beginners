def gcd(x, y): #x and y are two integers
    r = a % b
    if r == 0:
        return b
    if r == 1:
        return 1
    return gcf(b, r)

print(gcd(100, 20))
print(gcd(34723957, 1492598258327534))
