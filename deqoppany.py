minv = 1
maxv = 200

a = 9
b = 12
c = 25

def find_combo(i, a, b, c):
    z=0
    while c*z < maxv:
        y = 0
        while b*y < maxv:
            x = (i - b*y - c*z)/(a * 1.0)
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
    consecutives = []
    for i in range(minv, maxv):
        if find_combo(i, a, b, c):
            consecutives.append(i)
            print str(consecutives)
        else:
            consecutives = []
            last_false = i
        if len(consecutives) == a:
            print last_false
            return last_false

nuggets(minv, maxv)
