'''
Default arguments or optional arguments:

Default arguments/optional arguments are given values at the time of defining function. 
At the time of calling or invoking function if the values are not given for default arguments, 
it assign default values.

Syntax:
def <function-name>(arg1,arg2=value,arg3=value,…):
statement-1
statement-2

'''

# def draw_line(ch,l=30):
#     for i in range(l):
#         print(ch,end="")
#     print()

# def sort(s,order="accessding"):
#     if order=="accessding":
#         for i in range(len(s)):
#             for j in range(0,len(s)-1):
#                 if s[j]>s[j+1]:
#                     s[j],s[j+1]=s[j+1],s[j]
#     if order=="descending":
#         for i in range(len(s)):
#             for j in range (0,len(s)-1):
#                 if s[j]<s[j+1]:
#                     s[j],s[j+1]=s[j+1],s[j]
                    
# def sum_list(l):
#     count=0
#     for value in l:
#         count=count+value
#         return count

# def main():
#     draw_line("#")
#     draw_line("*",l=50)
#     list1=[2,4,1,9,5,7,8]
#     sort(list1)
#     print(list1)
#     draw_line("*",l=50)
#     sort(list1,"descending")
#     print(list1)
#     draw_line("*",l=50)
#     a=sum_list(list1)
#     print(f'sum of list1 is {a}')

# main()

# def simple_interset(amt,t,r=1.5):
#     si=(amt*t*r)/100
#     return si
# def main():
#     si1=simple_interset(50000,10,2.0)
#     si2=simple_interset(50000,10)
#     print(si1,si2)
    
# main()

#variable lengnth arguments


