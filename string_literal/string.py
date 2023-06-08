'''  
What is string?
    
String is a collection of characters and these characters can be alphabets,
digits or special characters.
String is a sequence data type, where the characters are organized in memory
in sequential order. String is a collection type.
str class is used to represent string object.

String literal or value is represented,
1. Within single quotes
2. Within double quotes
3. Within triple single quotes or double quotes

Within single quotes
Within single quotes we can represent single line string.
Within single quotes we can embed double quotes '''

#Within single quotes example.

# course='python language'
# print(type(course))

# s1='python is a 'scripting' langauge'
# print(s1)
# '''
# SyntaxError: invalid syntax
# PS E:\Python\python_nit\python_programes\string_literal> py .\string.py
#   File "E:\Python\python_nit\python_programes\string_literal\string.py", line 24    s1='python is a 'scripting' langauge'
#                      ^^^^^^^^^
# SyntaxError: invalid syntax
# PS E:\Python\python_nit\python_programes\string_literal> 
# '''
# s1='python is "scripting" language'
# print(s1)
# s5='course fee is "5000" for python'
# print(s5)


'''Within double quotes
Within double quotes we can represent single line string.
Within double quotes we can embed single quotes.'''

# str1="python programming language\n"

# str2="python is a
#   File "E:\Python\python_nit\python_programes\string_literal\string.py", line 45
#     str2="python is a
#          ^
# SyntaxError: unterminated string literal (detected at line 45)
# str3='"programming"\n'
# str4="python is 'scripting' langauge"
# print(str1, str3, str4)


'''Triple single quotes or double quotes
Triple single quotes or double quotes are used to represent multiline string.
In python the string which is represented in triple quotes is called doc string
# (document string).
'''

str1='''
python is a
"programming langauge",
'scripting langauges',
oop langauges
'''
print(str1)




