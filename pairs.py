def solution(s):
    pairs = []
    if len(s) != 0:
        for i in range(0, len(s), 2):
            split = s[i:i+2]
            pairs.append(split)
        if len(pairs[-1]) == 1:
            pairs[-1] = pairs[-1] + '_'
    return pairs

print solution('a')
