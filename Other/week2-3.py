a = [int(i) for i in input().split()]
n = int(input())
b=[]
for i in range(0,len(a)):
    if a[i]==n:
        b.append(a.index(a[i]))
        a[i]=""
if len(b)<=0:
    print("Отсутствует")
else: print(*sorted(b))