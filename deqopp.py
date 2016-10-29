minv = 0
maxv = 201

def nuggets(minv, maxv):
    # import pdb; pdb.set_trace()
    for i in range(minv, maxv):
        z = 0
        not_poss = []
        while 20*z < maxv:
            y = 0
            while 9*y < maxv:
                x = (i - 9*y - 20*z)/6.0
                if x.is_integer() and x >= 0:
                    x = int(x)
                    print "Test is true for " + str(i) + " x = " + str(x) + " y = " + str(y) + " z = " + str(z)
                else:
                    print "Test is not true for " + str(i) + " x = " + str(x) + " y = " + str(y) + " z = " + str(z)
                    not_poss.append(i)
                    print "List of not possibele values: " + str(i)
                y = y + 1
            z = z + 1

nuggets(minv, maxv)
