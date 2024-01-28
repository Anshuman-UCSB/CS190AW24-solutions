from collections import deque
r=lambda:map(int,input().split())
def solve(G, inDeg, P, l, optim=None):
	# print(G, inDeg, P, l)
	ans = 0
	while True:
		nOptim = deque()
		removed = optim or deque((n for n in G if inDeg[n]==0))
		while removed:
			r=removed.popleft()
			if P[r]!=l:
				nOptim.append(r)
				continue
			for c in G[r]:
				inDeg[c]-=1
				if inDeg[c] == 0:
					removed.append(c)
			del G[r]
		if len(G) == 0:
			break
		l=1-l
		optim=nOptim
		ans+=1
	return ans
answers = []
for _ in range(*r()):
	n,m=r()
	G={i+1:set() for i in range(n)}
	inDeg={i:0 for i in G}
	P=[None]+[v-1 for v in r()]
	for a,b in [r() for _ in range(m)]:
		G[a].add(b)
		inDeg[b]+=1
	answers.append(min(solve(dict(G), dict(inDeg), P, s) for s in (0,1)))
print(*answers,sep="\n")