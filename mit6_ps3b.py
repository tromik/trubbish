target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def countSubStringMatchRecursive(target, key):
    if target.find(key) == -1:
        return []
    keys = countSubStringMatchRecursive(target[target.find(key) + len(key):], key)
    for k in range(0, len(keys)):
        keys[k] = keys[k] + target.find(key) + len(key)
    return [target.find(key)] + keys


print str(countSubStringMatchRecursive(target2, key10))    
