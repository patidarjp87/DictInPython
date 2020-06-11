print("script to calculate sum of all dict values")
n=int(input('Enter ....how many pairs of key:value do you want to in your dict...?'))
d={eval(input('key')):eval(input('value')) for x in range(n)}
l=[]
s=0
for x in d.values():
    l.append(x)
for x in l:
    s=s+x
print("sum of values of dict is=  ",s)
input()
