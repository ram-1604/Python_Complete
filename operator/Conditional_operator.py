#*************conditionl & logical operator**********************
'''
Condtional Operator:
it is a ternary operator, it required 3 operands
Conditional operators are used to execute or evaluate operands based on
condition/Boolean expression.
opr1 if opr2 else opr3
if opr2 is True, it evaluates opr1
if opr2 is False, it evaluates opr3
opr2 is a condition or boolean expression

#################################################################################

Logical Operators:
These operators are used to combine two conditions or Boolean
expressions.
Logical operators are represented using keywords

'''

'''
and Truth table of and operator

Opr1    Opr2        Opr1 and Opr2
True    True        True
True    False       False
False   True        False
False   False       False

If first operand is True it evaluates second operand and return
result of second operand
If first operand is False, it does not evaluates second operand
it return result of first operand

'''
# a= 100>20 and 100>10
# b= 100>20 and 100>200
# c= 20>100 and 100>10
# d= 100 and 200
# e= 100 and 200 and 300
# f= 100 and 0 and 300
# g= "java" and "python"
# print(a,b,c,d,e,f,g)

'''
or Truth table of or operator

Opr1    Opr2    Opr1 or Opr2
True    True    True
True    False   True
False   True    True
False   False   False

If opr1 is True, it does not evaluate opr2, it returns value of
opr1
If opr1 is False, it evaluates opr2 and return result of opr2

'''

# a=True or False
# print(a)
# b=False or True
# print(b)
# c=100>20 or 100<20
# print(c)
# d=100 or 200 or 300
# print(d)
# e=0 or 200
# print(e)



# not to changes the result of value 
'''
opr1    not opr1
True    False
False   True

'''
a = True
print(not(a))