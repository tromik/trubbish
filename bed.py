# transmap = {"[":"]", "(":")", "{":"}"}
#
# def group_helper(exp, grp):
#     exp_flipped = transmap.get(exp, None)
#     if not grp:
#         return False
#     if grp[0] == exp_flipped:
#         return group_check(grp[1:])
#     elif not exp_flipped:
#         return False
#     if grp[0] in transmap.keys():
#         result = group_helper(grp[0], grp[1:])
#         if type(result) == bool:
#             return result
#         return group_helper(exp, result)
#     return False
#
# def group_check(s):
#     if not s:
#         return True
#     return group_helper(s[0], s[1:])

def group_check(s):
    while "{}" in s or "()" in s or "[]" in s:
       s = s.replace("{}","").replace("()","").replace("[]","")
    return not s

print(group_check(""))
print(group_check("{[([])]}"))
print("Below needs to be False")
print(group_check("({"))
print(group_check("{"))
print(group_check("]{}["))
