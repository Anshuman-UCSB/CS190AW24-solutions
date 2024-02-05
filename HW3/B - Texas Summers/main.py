from heapq import *
r=lambda:(*map(int,input().split()),)
N=r()[0]+2
V=[r()for _ in[0]*N]
P=[-1 for _ in V]
D=[float('inf')for _ in V]
def dist(a,b):
	(x1,y1),(x2,y2)=V[a],V[b]
	return (x2-x1)**2 + (y2-y1)**2
H=[(0,N-2)]
D[N-2]=0
S=[0]*N
while 1:
	d,n=heappop(H)
	if S[n]:continue
	S[n]=1
	if n==N-1:break
	for e in range(N):
		bid=d+dist(n,e)
		if bid < D[e]:
			D[e]=bid
			P[e]=n
			heappush(H,(bid,e))
p=[-1]
while p[-1]!=N-2:
	p+=[P[p[-1]]]
print(*p[-2:0:-1]or'-',sep='\n')