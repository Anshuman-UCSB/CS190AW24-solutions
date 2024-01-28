import sys
P=complex
G=set()
C=set()
for y,l in enumerate(sys.stdin.read().strip().splitlines()[1:]):
	for x,v in enumerate(l):
		if v=='W':continue
		(C if v=='C' else G).add(P(x,y))
def dfs(t,n):
	t|={n}
	for d in(1,-1,1j,-1j):
		if n+d in G|C and n+d not in t:
			dfs(t, n+d)
	return t
ans=0
while G:
	ans+=1
	n,*_=G
	G-=dfs(set(),n)
print(ans)