list_N =[]
list_div = []
for i in range(10):
    n = int(input())
    list_N.insert(i,n)
    
for j in range(10):
    nanugi = list_N[j] % 42
    if nanugi in list_div:
        pass
    else:
        list_div.append(nanugi)    
    

print(len(list_div))