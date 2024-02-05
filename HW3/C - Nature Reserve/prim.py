from collections import *
from heapq import *
r=lambda:map(int,input().split())
for _ in range(*r()):
	G=defaultdict(dict)
	N,M,L,S=r()
	stations={*r()}
	for _ in range(M):
		i,j,E=r()
		G[i][j]=G[j][i]=E+L
	out = set(G)-stations
	edges = []
	for a in stations:
		for b in out:
			if b in G[a] and G[a][b]:
				edges.append((G[a][b],b))
	best=defaultdict(lambda: float('inf'))
	heapify(edges)
	ans=0
	while out:
		c,n=heappop(edges)
		if n in stations:continue
		ans+=c
		out-={n}
		stations|={n}
		for e,v in G[n].items():
			if e in out:
				heappush(edges,(v,e))
			del G[e][n]
	print(ans)