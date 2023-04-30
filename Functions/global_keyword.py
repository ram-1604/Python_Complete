'''
global keyword:
The global statement is a declaration which holds for the entire current code block. 
It means that the listed identifiers are to be interpreted as globals. 
It would be impossible to assign to a global variable without global,
although free variables may refer to globals without being declared global.

if we want to modify th global varaible in the function we need to use global keyword.

'''
# x=10
# def fun1():
#     print(x)
# def fun2():
#     global x
#     x=200
#     #print(x)
    
# def main():
#     fun2()
#     fun1()
    
# main() 

#find the area of triangle

# def read():
#     global base,height
#     base=float(input("enter base:"))
#     height=float(input("enter height:"))
    
# def find_area():
#     area=0.5*base*height
#     print(f'area of trinagle is {area:.2f}')

# def main():
#     read()
#     find_area()

# main()


x=100
def fun1():
    print(x)
    global x
    x=200
    
def main():
    fun1()
main()

'''
The above code generate syntax error
In order access and update global variable with function, first we declare
those variables with global keyword
'''