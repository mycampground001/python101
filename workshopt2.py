import sys
sys.stdin = open("input.txt")

def is_line(x):
        cnt = 0
        for i in range(1,len(x)-1,2):
            if x[i]==x[i+1]:
                cnt+=1
        if cnt == len(x)//2-1:
            return True
        return False

def search_first(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][0] in arr[j] and i!=j:
                cnt+=1
        if cnt==0:
            return arr[i]
        else:
            cnt = 0

def solve(arr):
    tt=[]
    tt += search_first(arr)
    

    while True:
        
        if tt[-1] == arr[j][0]:
            tt += arr[i]
    return tt

for gg in range(int(input())):

    N = int(input())
    x = list(map(int,input().split()))
    arr = [[x[i+2*j] for i in range(2)] for j in range(N)]

    print(solve(arr))


