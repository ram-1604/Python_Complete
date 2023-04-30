# def draw_line(ch, l):
#     for i in range(l):
#         print(ch,end="")
#     print()
    
# def main():
#     draw_line("*",30)
#     draw_line("@",30)
#     draw_line("#",30)
#     draw_line("&",30)
#     draw_line(l=40, ch="^")
    
# main()


# write a functio to count no.of vowels in inpit string

def vowel_count(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count=count+1
    print(f'Vowels in the string are: {count}')

def main():
    str1=input("enter any string: ")
    vowel_count(str1)

main()

#return_keyword









    
