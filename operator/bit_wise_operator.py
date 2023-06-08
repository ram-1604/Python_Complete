'''
Right shift operator:
This operator is used for shifting number of bits towards
right side.
This operator is used for memory management
By shifting number of bits towards right side the value get
decremented. By removing bits

'''

# a=10
# b=a>>2
# print(a,b)
# print(bin(a),bin(b))

#Note:  Formula : num//2 pow n
# c=56
# d=c>>4
# print(c,d)
# print(bin(c),bin(d))


# set a bit program

# num=int(input("Enter a Number:"))
# print("Binary of enterd number is",bin(num))
# bit=int(input("Enter any bit position:"))
# # n=1<<(bit)
# # num=num^n
# num=(num | (1 << bit))
# print("The value after", bin(num), "bit is:", bin(bit))


# Python3 program to clear K-th bit of a number N

# num=int(input("Enter a Number:"))
# print("Binary of enterd number is",bin(num))
# bit=int(input("Enter any bit position:"))
# # n=1<<(bit)
# # num=num^n
# num=(num & ( ~(1 << (bit))))
# print("The value after", bin(num), "bit is:", bin(bit))


# Python3 program to toggle K-th bit of a number N

num=int(input("Enter a Number:"))
print("Binary of enterd number is",bin(num))
bit=int(input("Enter any bit position:"))
# n=1<<(bit)
# num=num^n
num=(num ^ (1 << (bit)))
print("The value after", bin(num), "bit is:", bin(bit))


# Python3 program to swap using bit wise operator.




