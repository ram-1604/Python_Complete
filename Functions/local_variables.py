'''
local Varibales: The variables declared inside function are called local variables
Local variables scope is within function, we cannot access these variables
outside function
Local variables memory is allocated when function is called and deallocated
after execution of function.
Example

'''

def fun1():
    x=100
    y=200
    print("im in fun1")
    print(x,y)
    print(id(x),id(y))
    
# def fun2():
#     print(x,y)  
    
def main():
    fun1()
    #fun2()
    
    
main()
x=2
y=3
print("i'm in main")
print(id(x),id(y))
print(x,y)

# stack are called static area and size is fixed all local varibales are allocated in stack.
#heap all objects are allocated in heap.