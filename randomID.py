from random import randint

def randomMessageID():
    res = ""
    for i in xrange(0,19):
        res += str(randint(0,9))
    return res
