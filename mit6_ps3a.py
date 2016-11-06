import string

target = 'abbadceefghiijklmmoooababbaghiikababbaceecee'
key = 'cee'

def countSubStringMatch(target, key):
    key_pos = []
    i = 1
    while target.find(key, i) > 0:
        print target.find(key, i)
        key_pos.append(target.find(key, i))
        i = key_pos[len(key_pos)-1] + 1
        print i
    return key_pos

key_pos = []
i = 1
def countSubStringMatchRecursive(target, key):
    if target.find(key) == -1:
        return []
    keys = countSubStringMatchRecursive(target[target.find(key):], key)
    for k in keys:
        k = k + target.find(k)
    return [target.find(key)] + keys

# print str(countSubStringMatch(target, key))

print str(countSubStringMatchRecursive(target, key))
