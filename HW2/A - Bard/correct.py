r=lambda:map(int,input().split())
N,=r()
A={person:set() for person in range(1,N+1)}
for song in range(*r()):
	_,*s = r()
	s = set(s)
	if 1 in s:
		for person in s:
			A[person].add(song)	
	else:
		allSongs = set()
		for person in s:
			allSongs|=A[person]
		for person in s:
			A[person]|=allSongs
print(*(p for p,s in A.items() if s==A[1]),sep='\n')