'''
Nested conditional operators
Using more than one conditional operator
Syntax:
opr1 if opr2 else opr3 if opr4 else opr5 if opr6 else opr7

'''

#Example:
# write a program to find max of three numbers
# n1=int(input("Enter n1 value:"))
# n2=int(input("Enter n2 value:"))
# n3=int(input("Enter n3 value:"))
# print(n1,"is max") if n1>n2 and n1>n3 else print(n2,"is max") if n2>n3 else print(n3,"is max")

# write a program or script to find input character is alphabet,digit or special character

ch = input("Enter any character:")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print(ch, " is alphabet") 
elif ch>='0' and ch<='9':
    print(ch, "is digit") 
else:
    print(ch,"is sepcial character")