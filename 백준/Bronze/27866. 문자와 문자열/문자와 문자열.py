a = list(input())
b = int(input())
# 1을 넣으면 a[0]
if 1 <= b <= len(a):
    print(a[b-1])
else:
    print(" index error")