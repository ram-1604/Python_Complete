'''
Nested Functions/Inner functions:
A function inside function is called nested function. Nested functions are used,
    1. Dividing functionality of one function into number of sub function
    2. Decorators
    3. Closures
Nested function can perform operation using the data of outer function
Nested function can access local variables of outer function but outer function cannot access local variables of inner function.
Nested function is used within outer function but cannot accessible outside outer function.

'''

# def fun1():
#     print("outer function/fun1")
#     def fun2():
#         print("inner function/Fun2")
#     fun2()
# def main():
#     fun1()
# main()


# def fun1():
#     x=100 # inside the fun1 which is accessable to fun2 since fun2 is also part of fuc1
#     def fun2():
#         y=110# which is local to function 2 and cannot accable out side the function
#         print("X=",x)
#     fun2()
#     # print("Y=",y)
# def main():
#     fun1()
# main()

'''
Python used LEGB serach method
LEGB
Python search names/variables using one searching method called LEGB.
LEGB stands,
L  Local
E  Enclosed Block
G  Global
B  Builtins module

'''


# x=100
# def fun1():
#     y=200
#     def fun2():
#         z=300
#         print(x,y,z,sep="\n")
#         print(__name__)
#     fun2()
# def main():
#     fun1()
    
# main()

'''
nonlocal
The nonlocal statement causes the listed identifiers to refer to previously
bound variables in the nearest enclosing scope excluding globals. This is
important because the default behavior for binding is to search the local
namespace first.
nonlocal variable-name,variable-name,…

'''

# def fun1():
#     x=100
#     def fun2():
#         nonlocal x
#         x=200
#         print(f'{x} value in side the fun2')
#     fun2()
#     print(f'{x} value in side the fun1')
# def main():
#     fun1()
    
# main()

# def calculator(n1,n2,oper):
#     res=0
#     def add():
#         nonlocal res
#         res=n1+n2
#     def sub():
#         nonlocal res
#         res=n1-n2
#     def mul():
#         nonlocal res
#         res=n1*n2
#     def div():
#         nonlocal res
#         res=n1/n2
#     if oper=='+':
#         add()
#     if oper=='-':
#         sub()
#     if oper=='*':
#         mul()
#     if oper=='/':
#         div()
#     return res

# def main():
#     num1=int(input("enter num1: "))
#     num2=int(input("enter num2: "))
#     opr=input("enter the operation: ")
#     result=calculator(num1,num2,opr)
#     print(f'Result of {num1} and {num2} is {result}')
# main()


#Decorator's

