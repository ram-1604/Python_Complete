'''
This data type is used to allocate memory for float value/real number. float
value is numeric value with precisions.
Note: all data types in python are dynamic size (OR) size of any data type
is unlimited.

float literal:a float value is represented in two formats or notations

1. Fixed notation/Standard notation
2. Exponent notation

Fixed notation or fixed format:
In fixed notation float value is represented by separating integer value and
decimal values using a decimal point.

Float data type reserve memory for 16 precisions. if more than 16
precisions it performs either rounding or truncating. If performs rounding if
value >=.5 else it truncates.
'''

a=257
b=257
print(a, b)
print(id(a),id(b))
f1=1.5
f2=1.5
print(a, b)
print(id(f1),id(f2))

'''
Exponent notation or scientific notation:
If the value is very large, it is represented exponent notation.
In exponent notation we use one special character “e” or “E”
'''
f1=123e-1
print(f1)
f2=1234e2
print(f2)
print(type(f1))
print(type(f2))
f3=1.45678e-3
print(f3)

