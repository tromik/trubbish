from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3
def  constrainedMatchPair(firstMatch,secondMatch,length):
    # import pdb; pdb.set_trace()
    match_pos_list = []
    for m1 in firstMatch:
        # print str(m1)
        for m2 in secondMatch:
            mhold = m1
            if m1 == 0 and m2 > 0:
                m1 = m2 - length - 1
            if m2 == 0 and m1 > 0:
                m2 = m1 + length + 1
            # print str(m2)
            # print 'Comparing: m1: ' + str(m1) + ' m2: ' +str(m2) + ' length: ' + str(length)
            if m2 == m1 + length + 1:
                match_pos_list.append(m1)
            m1 = mhold
    return match_pos_list

def subStringMatchExact(target, key):
    # import pdb; pdb.set_trace()
    if key == '':
         return [0]
    if target.find(key) == -1:
        return []
    keys = subStringMatchExact(target[target.find(key) + len(key):], key)
    for k in range(0, len(keys)):
        keys[k] = keys[k] + target.find(key) + len(key)
    return [target.find(key)] + keys

def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    # allAnswers = ()
    allAnswers = []
    # import pdb; pdb.set_trace()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        # import pdb; pdb.set_trace()
        if len(key) > 1:
            key1 = key[:miss]
            key2 = key[miss+1:]
        else:
            # if the key is one character set key1 to the character and key2 to blank,
            # this would work the same is key2 was the key and key1 was the blank
            key1 = key
            key2 = ''
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        filtered = list(set(filtered))
        # allAnswers = allAnswers + filtered
        allAnswers.append(filtered)
        print 'match1: ',match1
        print 'match2: ',match2
        print 'possible matches for: ',key1,key2,'start at',filtered
    return allAnswers

# import pdb; pdb.set_trace()
subStringMatchOneSub(target1, key13)

# def subStringMatchOneSub(target, key):
#     """search for all locations of key in target, with one substitution"""
#     allAnswers = []
#     for miss in range(0,len(key)):
#         # miss picks location for missing element
#         # key1 and key2 are substrings to match
#         import pdb; pdb.set_trace()
#         key1 = key[:miss]
#         print 'key1: ' + str(key1)
#         key2 = key[miss+1:]
#         print 'breaking key',key,'into',key1,key2
#         # match1 and match2 are tuples of locations of start of matches
#         # for each substring in target
#         match1 = subStringMatchExact(target,key1)
#         # match1 = subStringMatchExact(target,key1)
#         match2 = subStringMatchExact(target,key2)
#         # match2 = subStringMatchExact(target,key2)
#         # when we get here, we have two tuples of start points
#         # need to filter pairs to decide which are correct
#         # import pdb; pdb.set_trace()
#         # import pdb; pdb.set_trace()
#         # if not key1:
#         #     allAnswers = allAnswers + match2
#         # if not key2:
#         #     allAnswers = allAnswers + match1
#         # continue
#         # for m1 in match1:
#         #     for m2 in match2:
#         filtered = constrainedMatchPair(match1,match2,len(key1))
#         if filtered:
#             allAnswers = allAnswers + filtered
#             print 'match1',m1
#             print 'match2',m2
#         if not list(allAnswers):
#             print 'no possible matches'
#             # return ()
#         else:
#             print 'possible matches for',key1,key2,'start at', allAnswers
#     allAnswers.sort()
#     return tuple(set(list(allAnswers)))
