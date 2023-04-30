#Using a pair of square brackets to denote the empty list: []

# list1=[]
# print(list1)
# print(type(list1))

#Using square brackets, separating items with commas: [a], [a, b, c]

# list1=[10]
# list2=[10,20,30,40,50]
# list3=['ram',1604,27.8,2+3j]
# print(list1, list2, list3)
# print(type(list1),type(list2),type(list3))

##Using the type constructor: list() or list(iterable)

list1=list(range(10,110,10))
print(list1)
list2=list(list1)
print(list2)
list3=list("PYTHON")
print(list3)


