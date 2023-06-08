'''
What is generator?
A function which returns a generator iterator.
It looks like a normal function except that it contains yield expressions for
producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

yield keyword:
yield is a keyword, yield return value to caller pause execution of function
when iterator next() method is called it resumes back execute function

generator iterator:
An object created by a generator function.
Each yield temporarily suspends processing, remembering the location
execution state (including local variables and pending try-statements).
When the generator iterator resumes, it picks up where it left off

'''

# def fiun1():
#     yield 1
#     yield 10
#     yield 40
#     yield 20
#     yield 90
    
# def main():
#     f=fiun1()
#     print(f)
#     value1=next(f)
#     print(value1)
#     value2=next(f)
#     print(value2)
#     value3=next(f)
#     print(value3)
#     value4=next(f)
#     print(value4)
#     value5=next(f)
#     print(value5)
#     f=fiun1()
#     for value in f:
#         print(value,end=" ")
# main()

## create generator function which generates factorials within given range


# def factioral_gen(start,stop):
#     for num in range(start,stop+1):
#         fact=1
#         for i in range(1,num+1):
#             fact=fact*i
#         yield fact
# def main():
#     fact=factioral_gen(1,5)
#     sum=0
#     for value in fact :
#         print(value, end=" ")
#         sum=sum+value
#     print()
#     print(f'sum of all factorial is {sum}')
# main()

# import random
# def otp_generator():
#     while True:
#         otp=random.randint(100000,999999)
#         yield otp
# def main():
#     otpg=otp_generator() # genreator iterator object
#     otp1=next(otpg)
#     print(otp1)
#     otp2=next(otpg)
#     print(otp2)
# main()

#Pass word generator WA
# def password_generator():
    



# odd=(num for num in range(1,10,2))
# print(odd)
# next(odd)
# print(odd)
# next(odd)
# print(odd)
# srt=(num**2 for num in range(1,6,1))
# print(srt)

#lamda function