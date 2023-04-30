'''
“complex” class or data type used to represent complex numbers.
Complex number is having two values.
1. Real
2. Imag
Syntax of representing complex number
real+imagj

syntax:
1) complex(Value)
2) complex(real=0.0, imag=0.0)

'''
#syntax-1

# s="1+2j"
# c=complex(s)
# print(s,c)

#syntax-2

# c=complex(2.3,3.4)
# c1=complex(1,3)
# print(c, c1)

# reading  only real & imaginary vales. here default values are zeronfor complex
comp=2
comp1=2j
print(type(comp), type(comp1))
print(comp.imag, comp.real)
print(comp1.imag, comp1.real)
