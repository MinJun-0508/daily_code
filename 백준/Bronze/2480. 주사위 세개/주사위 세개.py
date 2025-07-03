a,b,c = map(int, input().split())
lotto = [a,b,c]
if a==b==c:
    award = 10000+a*1000
    print(award)
elif a==b:
    award = 1000 + a*100
    print(award)
elif a==c:
    award = 1000 + a*100
    print(award)
elif b==c:
    award = 1000 + b*100
    print(award)
else:
    for i in range(2,0,-1):
        for j in range(0,i,1):
            if lotto[j] > lotto[j+1]:
                temp = lotto[j]
                lotto[j] = lotto[j+1]
                lotto[j+1] = temp
    award = lotto[2] *100
    print(award)