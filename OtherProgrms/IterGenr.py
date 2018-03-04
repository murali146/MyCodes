def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        print "before yield --- " + str(i)
        yield i
        i = i + 1
        print "after yield >>> " + str(i)

def squares():
    for i in integers():
        print "i am in sqr:::: " + str(i)
        yield i * i



def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    print " SEQUENCE - " + str(seq)
    result = []

    try:
        for i in range(n):
            result.append(seq.next())
            print "Result <<<< " + str(result)
    except StopIteration:
        pass
    return result



print " PYTHOGORAS TRIPLET "

pyt = ((x, y, z) for z in integers() for y in xrange(1, z) for x in range(1, y) if x*x + y*y == z*z)
print take(10, pyt)

#print take(9, squares()) # prints [1, 4, 9, 16, 25]