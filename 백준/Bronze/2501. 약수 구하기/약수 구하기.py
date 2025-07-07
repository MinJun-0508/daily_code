N,K = map(int,input().split())

a_feature = []
for i in range(1,N + 1):
    if N % i == 0 :
        a_feature.append(i)
    else:
        pass 

if K > len(a_feature):
    print("0")
else:
    print(a_feature[K-1])