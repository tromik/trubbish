minv = 1
maxv = 100

def find_combo(i):
    z=0
    while 20*z < maxv:
        y = 0
        while 9*y < maxv:
            x = (i - 9*y - 20*z)/6.0
            if x.is_integer() and x >= 0:
                x = int(x)
                # print "Test is true for " + str(i) + " x = " + str(x) + " y = " + str(y) + " z = " + str(z)
                return True
            # elif x >= 0:
                # print "Test is not true for " + str(i) + " x = " + str(x) + " y = " + str(y) + " z = " + str(z)
            y = y + 1
        z = z + 1
    return False

def nuggets(minv, maxv):
    # import pdb; pdb.set_trace()
    last_false = None
    six_consecutives = []
    for i in range(minv, maxv):
        if find_combo(i):
            six_consecutives.append(i)
            print str(six_consecutives)
        else:
            six_consecutives = []
            last_false = i
        if len(six_consecutives) == 6:
            print last_false
            return last_false

nuggets(minv, maxv)
