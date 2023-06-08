'''
Lamda Function/expression :
Lambda Functions or lambda expressions
Lambda function is anonymous function
A function which does not have any name is called anonymous function
Lambda function is having only one statement
Lambda functions are used as a higher order functions
A function which is defined as argument to another function is called higher order function

Syntax:
lambda [arg1,arg2,..]:expression

'''
# def main():
#     a=lambda:print("lambda function with a varibale ")
#     b=lambda:print("lambda function with b variable")
#     print(a)
#     print(b)
#     a()
#     b()
#     a()
#     a()
# main()


'''
diff b/w function and lamda function:

Function                                        Lambda function
Function is with name                           Lambda function is without name
Function is written using def                   Lambda function written using keyword lambda keyword
Function can have multiplestatements            Lambda expression is having only  one statement
Function cannot be defined as an argument       Lambda function is defined as anargument/can be used as higher order function
return statement is used to return value        return statement is not allowed

'''

# def main():
#     add=lambda a,b:a+b
#     sub=lambda a,b:a-b
#     res1=add(10,20)
#     res2=sub(10,5)
#     print(res1)
#     print(res2)
#     find_max=lambda a,b:a if a>b else b
#     res3=find_max(100,10)
#     res4=find_max(20,50)
#     print(res3,res4)
# main()

# 

# Lamda are used in the some pre-defined functions eg: filter

'''
filter(function, iterable)
Construct an iterator from those elements of iterable for which function
returns true. iterable may be either a sequence, a container which supports
iteration, or an iterator. If function is None, the identity function is assumed,
that is, all elements of iterable that are false are removed.

'''
# def main():
#     list1=[1,7,9,2,4,8,45,76,89,23,55,67,98,23,45,54,76,67,89,22,33]
#     list2=list(filter(lambda n:n%7==0,list1))
#     list3=list(filter(lambda n:n%2==0,list1))
#     list4=list(filter(lambda n:n%2!=0,list1))
#     print(f'original list is {list1}')
#     print(f'list which contain divisible by 7 {list2}')
#     print(f'list which contain only even number {list3}')
#     print(f'list which contain odd number {list4}')
# main()




'''
map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, yielding the
results. If additional iterable arguments are passed, function must take that
many arguments and is applied to the items from all iterables in parallel.
With multiple iterables, the iterator stops when the shortest iterable is
exhausted.

'''
#Add of elements in the 2 List and print in 3rd list

# def main():
#     l1=[1,2,3,4,5]
#     l2=[10,20,30,40,50]
#     l3=list(map(lambda a,b:a+b,l1,l2))
#     print(l1,l2,l3,sep="\n")
#     l4=["45","56","65","76","89"]
#     l5=list(map(int,l4))
#     print(l4,l5,sep="\n")
#     l6=list(map(int,input().split(" "))) # "10 20 30 40 50".split(" ") ==>["10","20","30","40","50"]
#     print(l6)
# main()



#reduce function will reduce the any iteraror based on the logic that we written.

'''
functools.reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of iterable, from
left to right, so as to reduce the iterable to a single value. For example,
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The
left argument, x, is the accumulated value and the right argument, y, is the
update value from the iterable. If the optional initializer is present, it is
placed before the items of the iterable in the calculation, and serves as a
default when the iterable is empty. If initializer is not given and iterable
contains only one item, the first item is returned.

'''


# import functools
# def main():
#     list1=list(range(10,110,10)) # 10 20 30 40 50 60 70 80 90 100
#     print(list1)
#     m=functools.reduce(lambda a,b:a if a>b else b,list1)
#     print(m)
#     n=functools.reduce(lambda a,b:a if a<b else b,list1)
#     print(n)
#     s=functools.reduce(lambda a,b:a+b,list1)
#     print(s)
# main()

#Modules & Pacakges
