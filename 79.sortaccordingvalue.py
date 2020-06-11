print(" script to sort dict according to value")
n=int(input('Enter ....how many pairs of key:value do you want to in your dict...?'))
d={eval(input('key')):eval(input('value')) for x in range(n)}
l=[]
d1={}
for x in d.values():
    l.append(x)
l.sort()
i=0
while i!=n:
 for x in d.keys():
    if d[x]==l[i]:
        d1.update({x:l[i]})
        i+=1
        if i==n:
            break
    
print("sorted dict according values is :::\n",d1)   
input()