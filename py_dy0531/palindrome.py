# def palindrom_check1(pstring):
#     rstring = list(reversed(pstring))
#     ispal = True
#     for k in range(len(pstring)):
#         if pstring[k] != rstring[k]:
#             ispal = False
#     return ispal

# pstringList = ['역삼역','구로구','mom','기러기','비둘기','기특한','racer','father','봄','여름']

# for s in pstringList:
#     print('{0} = {1}'.format(s, palindrom_check1(s)))

# def palindrom_check2(s):
#     qu = []
#     st = []
#     for x in s:
#         if x.isalpha():
#             qu.append(x.lower())
#             st.append(x.lower())
#         while qu:
#             if qu.pop(0) != st.pop():
#                 return False
#         return True

# pstringList = ['역삼역','구로구','mom','기러기','비둘기','기특한','racer','father','봄','여름']

# for s in pstringList:
#     print('{0} = {1}'.format(s, palindrom_check2(s)))

from collections import deque

def palindrom_check3(pstring):
    qu = []
    st = []
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
        while qu:
            if qu.pop(0) != st.pop():
                return False
        return True
    
pstringList = ['역삼역','구로구','mom','기러기','비둘기','기특한','racer','father','봄','여름']

for s in pstringList:
    print('{0} = {1}'.format(s, palindrom_check3(s)))