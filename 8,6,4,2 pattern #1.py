#8,6,4,2 pattern
n=int(input('Max number: '))
for i in range(n,-1,-2):
    for j in range(n,i,-2):
        print(j,end='')
    print()
