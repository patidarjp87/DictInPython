print("program to learn how to take input from user in list,tuple,set and dict .\n Note that enter everything as it is as you want to see in your list/tuple/set/dict")
t=tuple([eval(x) for x in input('Enter tuple elements by seperator space\n').split()])
print(t)
t=set([eval(x) for x in input('Enter set elements by seperator space\n').split()])
print(t)
t=[eval(x) for x in input('Enter list elements by seperator space\n').split()]
print(t)
n=int(input('Enter ....how many pairs of key:value do you want to in your dict...?'))
d={eval(input('key')):eval(input('value')) for x in range(n)}
print(d)
input()

