print("script to print dict items in diffresnt lines ")
n=int(input('Enter ....how many pairs of key:value do you want to in your dict...?'))
d={eval(input('key')):eval(input('value')) for x in range(n)}
print('key:value')
for x,y in d.items():
    print(x,':',y)
input()