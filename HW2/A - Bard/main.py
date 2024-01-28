r=lambda:map(int,input().split())
N,=r()
A={*range(1,N+1)}
for _ in range(*r()):
	_,*s = r()
	s = set(s)
	if 1 in s:
		A&=s
	else:
		A|=s
	# print(A,s)
print(*sorted(A),sep='\n')