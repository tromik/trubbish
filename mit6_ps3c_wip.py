target = 'ATGACATGCACAAGTATGCAT'
key = 'ATGC'

key1 = 'A'
key2 = 'GC'

def countSubStringMatchRecursive(target, key):
    if target.find(key) == -1:
        return []
    keys = countSubStringMatchRecursive(target[target.find(key) + len(key):], key)
    for k in range(0, len(keys)):
        keys[k] = keys[k] + target.find(key) + len(key)
    return [target.find(key)] + keys

starts1 = countSubStringMatchRecursive(target, key1)
starts2 = countSubStringMatchRecursive(target, key2)
# print str(countSubStringMatchRecursive(target2, key10))

print 'Starts1: ' + str(starts1)
print 'Starts2: ' + str(starts2)
