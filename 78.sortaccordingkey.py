print(" script to sort dict according to key")
n=int(input('Enter ....how many pairs of key:value do you want to in your dict...?'))
d={eval(input('key')):eval(input('value')) for x in range(n)}
l=sorted(d)
d1={}
for x in l:
    d1[x]=d[x]
print('sorted dict according to key is ::: ',d1)
input()