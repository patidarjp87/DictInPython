print(" script to sort dict according to value")
n=int(input('Enter ....how many pairs of key:value do you want to in your dict...?'))
d={eval(input('key')):eval(input('value')) for x in range(n)}
l=[]
d1={}
for x in d.values():
    l.append(x)
l.sort()
i=0
while r!=len(d):
 for x in d.keys():
    if d[x]==l[i] and d[x] not in d1:
        d1.update({x:l[i]})
        r+=1
        i+=1
    
print("sorted dict according values is :::",d1)   
input()