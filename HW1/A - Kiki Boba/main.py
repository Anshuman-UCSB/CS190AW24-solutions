from collections import Counter
c = Counter(input())
if c['k'] == c['b'] == 0:
    print("none")
elif c['k']>c['b']:
    print("kiki")
elif c['k']==c['b']:
    print("boki")
elif c['k']<c['b']:
    print("boba")