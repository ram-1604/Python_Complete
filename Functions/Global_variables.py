'''
Global variables:
Variables declared outside the function are called global variables
Global variables memory is allocated when program is executed/run.

'''

# x=100 # 1
# y=200 # 2
# def fun1():
#     print(x,y) # 100 200
# def fun2():
#     print(x,y) # 100 200
# print(x,y) # 100 200 ==> 3
# def main():
#     print(x,y) # 100 200 ==> 5
#     fun1() # 6
#     fun2() # 7

# main() # 4


# def fun1():
#     print(x,y)
# x=100
# y=200

# def main():
#     fun1()

# main()


#devloping simple calculator
# n1=int(input("enetr first number:"))
# n2=int(input("enter seond number:"))
# def add():
#     print(f'sum is {n1+n2}')
# def sub():
#     print(f'diff is {n1-n2}')
# def mul():
#     print(f'multiply is {n1*n2}')
# def div():
#     print(f'division is {n1/n2}')
# def mod():
#     print(f'modulas is {n1%n2}')
    
# def main():
#     add()
#     sub()
#     mul()
#     div()
#     mod()
    
# main()


x=10
def fun1():
    x=3
    y=4
    print(x,y)
def fun2():
    x=8
    z=6
    print(x,z)
def main():
    fun1()
    fun2()
main()

#Global keyword.
