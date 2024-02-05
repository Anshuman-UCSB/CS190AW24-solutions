from collections import *
r=lambda:map(int,input().split())
for _ in range(*r()):
	N,M,L,S=r()
	P=list(range(N+1))
	Sz=[1]*(N+1)
	def rep(n):
		if P[n]!=n:
			P[n]=rep(P[n])
		return P[n]
	def join(a,b):
		a=rep(a)
		b=rep(b)
		if(Sz[b]>Sz[a]):a,b=b,a
		P[b]=a
		Sz[a]+=Sz[b]
	[join(0,s)for s in r()]
	H=defaultdict(list)
	for i,j,E in [r()for _ in[0]*M]:
		if P[i]==P[j]:continue
		H[E].append((i,j))
	ans=0
	N-=S
	T=N
	for k in sorted(H):
		for i,j in H[k]:
			if rep(i)==rep(j):continue
			join(i,j)
			ans+=k
			T-=1
			if T==0:break
	print(ans+L*N)