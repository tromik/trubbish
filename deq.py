minv = 0
maxv = 501

def nuggets(minv, maxv):
    # import pdb; pdb.set_trace()
    for i in range(minv, maxv):
        z = 0
        while 20*z < maxv:
            y = 0
            while 9*y < maxv:
                x = (i - 9*y - 20*z)/6.0
                if x.is_integer() and x >= 0:
                    x = int(x)
                    print "Test is true for " + str(i) + " x = " + str(x) + " y = " + str(y) + " z = " + str(z)
                y = y + 1
            z = z + 1

nuggets(minv, maxv)
