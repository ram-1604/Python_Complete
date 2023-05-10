'''
Decorators
A function returning another function, usually applied as a function transformation using the @wrapper syntax.
Common examples for decorators are classmethod() and staticmethod().

Decorators are used to extend the functionality of existing function without modifying it.
Decorators are build using nested function
Decorator function receive a function as input And transform into another function using nested function
And return nested function

Syntax:
    def <function-name>(function):
        def <nested-function-name>([args]):
            statement-1
            statement-2
            may include functionality of old function
        return <nested function>

    
'''
# def box(f):
#     def new_fun1():
#         print("*****************************")
#         f()
#         print("#############################")
#     return new_fun1

# @box
# def fun1():
#     print("Hello world")

# def main():
#     # nf=box(fun1)
#     # nf()
#     fun1()

# main()


# def smart_division(f):
#     def new_division(n1,n2):
#         if n2==0:
#             print(f'denominator 0 cannot be divisiable')
#             return 0
#         else:
#             return f(n1,n2)
#     return new_division

# @smart_division
# def dvision(n1,n2):
#     n3=n1/n2
#     return n3


# def main():
#     a=int(input("enter the n1 value: "))
#     b=int(input("enter the n2 value: "))
#     c=dvision(a,b)
#     print(a,b,c,sep="\n")
    
# main()


# def fun3(function):
#     def fun4():
#         print("decorator")
#         function()
#     return fun4()
        

# @fun3
# def fun1():
#     print("fun1")
# @fun3
# def fun2():
#     print("fun2")
    
# def main():
#     fun1()
#     fun2()
    
# main()



#clousers




