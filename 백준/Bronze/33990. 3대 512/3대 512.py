N = int(input())
list_ORM = []
for i in range(N):
    A,B,C = map(int,input().split())
    if (A+B+C) >= 512:
        list_ORM.append(A+B+C)
    else:
        pass
if list_ORM == []:
    print("-1")

else:
    print(min(list_ORM))
