'''
Keyword arguments
The function required input as key and value is defined with keyword arguments
Keyword arguments are prefix with **
Keyword argument is of type dictionary
Keyword arguments are used to perform two operations
    1. Invoking function by sending key and value
    2. For manipulating dictionaries

'''

# def fun1(**a):
#     print(a,type(a),sep="\n")

# def main():
#     fun1()
#     fun1(x=10)
#     fun1(x=10,y=20,z=30)
# main()


# def add(**kwargs):
#     total=0
#     for key,value in kwargs.items():
#         total=total+value
#         print(f'{key}----->{value}')
#     print(f'total is {total}')
    
# def main():
#     add(x=10,y=20)
    
# main()

# def add(*args,**kwargs):
#     total=0
#     if len(args)!=0:
#         for value in args:
#             total=total+value
#             print(f'total value is {value}')
            
#     if len(kwargs)!=0:
#         for key,value in kwargs.items():
#             total=total+value
#             print(f'{key}----->{value}')
#     print(f'total is {total}')
    
# def main():
#   add(10,20)
#   add(x=30,y=40)
# main()


# def display(**k):
#     tot=0
#     for year,sales in k.items():
#         print(f'{year}--->{sales}')
#         tot=tot+sales
#     print(f'Total Sales {tot}')
    
# def main():
#     sales_dict={'2000':450000,'2001':540000,'2002':560000}
#     display(**sales_dict) # dictionary unpacking
# main()
    
#Nested Functions    
