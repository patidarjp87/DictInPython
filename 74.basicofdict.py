print("basic program of dict learn how to take input from user")
n=int(input('Enter.....how many pairs do you want to store...?\n'))
l=[]
d={}
for x in range(1,n+1):
    print("enter key no.",x,end=' ')
    l.append(eval(input()))
for x in l:
    print("Enter value for key ",x,end=' ')
    d[x]=eval(input())
print(d)
input()