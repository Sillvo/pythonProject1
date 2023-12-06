n = int(input())
s = list(range(1,n+1))
s1=[]
i=0
while i<(len(s)):
    j=0
    while j<(s[i]):
        s1.append(s[i])
        j=j+1
    i=i+1
print(*s1[:n])