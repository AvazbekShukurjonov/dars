num=5
for i in  range(1, num+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

for i in range(num,0,-1):
    for j in range(0,i-1):
        print('*', end=' ')
    print()