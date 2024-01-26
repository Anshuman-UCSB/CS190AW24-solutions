r=lambda:list(map(int,input().split()))
for _ in[0]*r()[0]:
	l,n=r()
	p=[]
	while len(p)<n:
		p.extend(r())
	s=b=0
	for i in p:
		s=max(s,min(i,l-i))
		b=max(b,max(i,l-i))
	print(s,b)