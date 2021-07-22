# this code get tle

def divisiorK(N):
    i=1
    divisors=[]
    while (i*i<=N):
        if (N%i==0):
            if N//i!=i:
                divisors.append(N//i)
            divisors.append(i)
        i+=1
    return divisors


def t1(lst,K):
    cnt=0
    for i in lst:
        if K%i==0:
            cnt+=1
    return cnt


def t2(lst,K):
    cnt=0
    for i in lst:
        if i%K==0:
            cnt+=1
    return cnt


def t3(lst,K):
    cnt=0
    for i in lst:
        if i%K!=0:
            cnt+=1
    return cnt


n,q=map(int,input().split())
N_divisors=divisiorK(n)
for _ in range(q):
    t,k=map(int,input().split())
    if t==1:
        print(t1(N_divisors,k))
    elif t==2:
        print(t2(N_divisors,k))
    else:
        print(t3(N_divisors,k))
