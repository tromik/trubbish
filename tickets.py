def tick(people):
    total = 0
    tf = 0
    ff = 0


    for i in people:
        if i == 25:
            tf += 1
            poss = True
        elif i == 50:
            if tf == 0:
                poss = False
                break
            else:
                tf -= 1
                ff += 1
                poss = True
        elif i == 100:
            if (tf >=1 and ff >= 1):
                ff -= 1
                tf -= 1
                poss = True
            elif (tf >= 3):
                tf -= 3
                poss = True
            else:
                poss = False
                break

    if poss == True:
        return "YES"
    else:
        return "NO"



















def tickets(people):
    # import pdb; pdb.set_trace()
    print "HIIIIIIIII"
    return tick(people)

print tickets([25, 25, 50])
print tickets([25, 25, 50, 25, 100, 25, 25, 50])
print tickets([50, 25, 50])
print tickets([25, 50, 100])
