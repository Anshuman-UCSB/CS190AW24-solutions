from collections import *
from heapq import *
r=lambda:map(int,input().split())
N,m,e=r()
G=defaultdict(dict)
for _ in[0]*m:
	a,b,l=r()
	G[a][b]=G[b][a]=l
E={*r()}
b,p=r()
Ct={}
H=[(0,p)]
while len(Ct)<N:
	t,n=heappop(H)
	if n in Ct:continue
	Ct[n]=t
	for e,c in G[n].items():
		if e not in Ct:
			heappush(H,(c/160+t,e))
def solve(s):
	T={}
	H=[(0,b)]
	while H:
		t,n=heappop(H)
		if n in T:continue
		if n in E:return 1
		T[n]=t
		for e,c in G[n].items():
			c/=s
			if e not in T and c+t<Ct[e]:
				heappush(H,(c+t,e))
	return 0
if 1-solve(9e9):
	print("IMPOSSIBLE")
	exit()
L,H=0,1
while 1-solve(H):
	L=H
	H*=2
while H-L>1e-6:
	m=(H+L)/2
	if solve(m):
		H=m
	else:L=m
print((L+H)/2)