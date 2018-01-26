from itertools import count
def floyd(n):
    x = ((n**2 + n)/2)
    last_row = ' '.join(str(s) for s in xrange(x-(n-1), x+1))
    width = len(last_row)
    c = count(1)
    for x in xrange(1, n):
        line = ' '.join(str(next(c)) for _ in xrange(x))
        print "{:^{}}".format(line, width)
    print last_row
