B=lambda:map(int,input().split())
E,=B()
C={1}
for D in range(*B()):
    D,*A=B();A={*A};C&=A if{1}&A else C|=A
print(*sorted(C),sep='\n')