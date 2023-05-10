'''
Variable length arguments:

An argument which receive more than one value is called variable length argument
Variable length argument is prefix with *
Variable length argument is type of tuple
Variable length argument receive 0 or more
If function required more than input to perform operation use variable length arguments
A function is defined with only one variable length argument


Note: A function must have single varaible lengnth aruguments, we can't send the multiple varibale lenghth arguments
If we are writting more thn 1 the syntax error


'''

# def fun1(*a):
#     print(a,type(a),sep="\n")
    
# def main():
#     fun1()
#     fun1(10,20)
#     fun1(10,"python",1+2j,22.45)
# main()
    
#find max of n number

# def maxmium(*num):
#     m=0
#     for value in num:
#         if value>m:
#             m=value
#     return m

# def main():
#     res=maxmium(10,20)
#     res1=maxmium(10,20,30)
#     res2=maxmium(40,30,20,80)
#     print(res,res1,res2,sep="\n")
    
# main()

# def fun1(a,*b,c=10):
#     print(a,b,c)
    
# def fun2(*b,a,c=10):
#     print(a,b,c)

# def main():
#     fun1(100)
#     fun1(100,200)
#     fun1(100,200,300)
#     fun1(100,200,300,c=400)
#     fun2(a=100)
#     fun2(a=100,200)
#     fun2(100,200,300)
#     fun2(100,200,300,c=400)
    
# main()


'''
if we missed the order of argumments 

PS E:\Python\python_nit\python_programes\Functions> py .\variable_length.py
  File "E:\Python\python_nit\python_programes\Functions\variable_length.py", line 56
    fun2(a=100,200)
                  ^
SyntaxError: positional argument follows keyword argument

'''
'''
The order of defining arguments are
1. Required arguments
2. Variable length arguments
3. Keyword arguments
4. Default arguments

'''

# keyword arguments





    
    
    
    
    
    
    
    
    
    




