r=lambda:map(int,input().split())
a=0
cauldron = {}
cauldronSizes = {}
n=500_002
for _ in range(*r()):
	_,*ing=r()
	groups = set()
	size=0
	for i in ing:
		if i not in cauldron:
			cauldron[i] = i
			cauldronSizes[i]=1
		rep = cauldron[i]
		if rep not in groups:
			groups.add(rep)
			size+=cauldronSizes[rep]
	if size == len(ing):
		a+=1
		for i in ing:
			cauldron[i]=n
		cauldronSizes[n]=size
		n+=1
print(a)