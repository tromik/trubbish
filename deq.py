
for i in range(1, 60):
    for x in range(0, 100):
        for y in range(0, 100):
            for z in range(0, 100):
                if 6*x + 9*y + 20*z == i:
                    print "Test is true for " + str(i) + " x = " + str(x) + " y = " + str(y) + " z = " + str(z)
