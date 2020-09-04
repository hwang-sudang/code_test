# inputs
h,w = map(int,input().split(' ')) # 격자 사이즈
n = int(input()) # Test Case

# 배경 지정
arr = [[0]*w for i in range(h)] # 0으로 가득찬 배경 지정


# 테스트 케이스만큼 포문 돌린다.
for _ in range(n):
    l,d,x,y = map(int,input().split(' '))
    x-=1; y-=1 # 인덱스 때문에
    
    for j in range(l):
        if d==1:  # 세로형
            arr[x+j][y]+=1
        else: # 가로형
            arr[x][y+j]+=1
            

# 출력
for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()
    