
''' 
ord():
it is a predefined function in python, which return ascii value or input
character
'''
# ord(‘a’)  97
# ord(‘A’)  65
# ord(‘b’)  98
# ord(‘B’)  66
'''
chr():
it is a predefined function in python, which return character value of input
ascii value
'''
# chr(65)  A
# chr(66)  B
# chr(97)  a
# chr(98)  b
# Example:
# write a program to convert input character into uppercase or lowercase
ch=input("enter any character:")
res=chr(ord(ch)-32) if ch>='a' and ch<='z' else chr(ord(ch)+32) if ch>='A' and ch<='Z' else "invalid input" 
print("upper case of", ch, "is", res)