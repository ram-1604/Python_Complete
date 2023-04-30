# Slicing
# Slicing is process of reading more than one value/element from list
# Slicing return another list by copying all the elements or items
# Slicing is done using two approaches
# 1. Slice operator
# 2. Slice object
# Slicing required the following values
# 1. Start index
# 2. Stop index
# 3. Step
# Slicing uses internally range for generating indexes
# Slice operator
# Syntax1: list-name[start:stop:step]
# Syntax2: list-name[start::]
# Syntax-3: list-name[:stop:]
# Syntax4: list-name[::step]
# Syntax5:list-name[start:stop]
# Syntax6: list-name[start::step]
# Syntax7: list-name[:stop:step]
# Syntax8: list-name[::]
# Syntax9: list-name[:]

# *******************************************************************************************
# Syntax8: list-name[::]
# This syntax uses default values
# start: 0
# stop: length of list
# step: +1
# This syntax read all the value from list left to right (OR) create copy of the list
# *******************************************************************************************

# list1=list(range(10,110,10))
# print(list1)
# list2=list1[::]
# print(list2)

# *******************************************************************************************

# Syntax9: list-name[:]
# It is same as syntax-8

# list1=list(range(10,110,10))
# print(list1)
# list2=list1[:]
# print(list2)
# *******************************************************************************************

# Syntax4: list-name[::step]
# In this syntax start and stop values are taken based on step
# If step +ve start=0,stop=len(list)
# If step –ve start=-1,stop=-(len(list)+1)

# list1=list(range(10,210,10))
# print(list1)
# list2=list1[::1]
# print(list2)
# list3=list1[::2]
# print(list3)
# list4=list1[::3]
# print(list4)
# list5=list1[::-3]
# print(list5)
# list6=list1[::-2]
# print(list6)
# list7=list1[::-1]
# print(list7)

#******************************************************************************************

#Syntax5: list-name[start:stop]
# list1=list(range(10,210,20))
# print(list1)
# list2=list1[0:7]
# print(list2)
# list3=list1[1:5]
# print(list3)

#*********************************************************************************************************

# Syntax6: list-name[start::step]
# Syntax7: list-name[:stop:step]

list1=list(range(10,210,10))
print(list1)
list2=list1[::-1] 
print(list2)   
list3=list1[:7:1]
print(list3)






