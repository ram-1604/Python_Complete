'''
Closures
Closure is a special function
Closure function returns a function
Closure is an inner function which perform operation uses data of outer function
If you want to perform different operations using data of outer function then
use closures

Syntax:
def outer_function([arg1,arg2,…]):
    def inner_function([arg1,arg2,..]):
        statement-1
        statement-2
    return inner function/closure-function

'''
# def find_power(num):
#     def power(p):
#         return num**p

#     return power

# def main():
#     pow1=find_power(2)
#     res1=pow1(2)
#     res2=pow1(3)
#     print(res1,res2)
#     pow2=find_power(3)
#     r1=pow2(2)
#     r2=pow2(3)
#     print(r1,r2)
# main()


# def calculator(n1,n2):
#     def calculate(opr):
#         if opr=='+':
#             return n1+n2
#         if opr=='-':
#             return n1-n2
#         if opr=='/':
#             return n1/n1
#     return calculate
# def main():
#     cal=calculator(30,2)
#     res1=cal('+')
#     res2=cal('-')
#     print(res1,res2)
#     cal2=calculator(50,5)
#     r1=cal2('+')
#     r2=cal2('-')
#     print(r1,r2)
# main()




def draw_line(ch):
    def draw(l):
        for i in range(l):
            print(ch,end='')
        print()
    return draw
def main():
    draw1=draw_line('*')
    draw1(10)
    draw1(50)
    draw1(30)
    draw2=draw_line('$')
    draw2(5)
    draw2(10)
    draw1(50)
main() 
