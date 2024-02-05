from collections import defaultdict
r=lambda:map(int,input().split())
n,m=r()
G = defaultdict(lambda: [set(),set()])
for _ in range(m):
    a,b=r()
    G[abs(a)][a>0].add(b)
ends = set()
q = [(1,0)] # pos, has bugged
seen = set()
while q:
    p,f = q.pop()
    if (p,f) in seen: continue
    seen.add((p,f))
    if f==0:
        q.extend([(e,1) for e in G[p][1]])
    q.extend([(e,f) for e in G[p][0]])
    if G[p][0]==set():
        ends.add(p)
print(len(ends))