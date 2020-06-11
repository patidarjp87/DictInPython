print("script to create dict in which student roll n0. as key and name as value")
n=int(input("Enter.....how many students roll no or name do you want to add in dict...?\n"))
d={eval(input('student roll no. ')):eval(input(' student name in double/single quotes ')) for x in range(n)}
print('list of student roll no. and name \n',d)
input()