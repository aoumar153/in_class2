
def r(s):
    s1 = ''.join(reversed(s))
    return s1

def p(inp):
    re = []
    #inp = input("Enter a string:  ")
    l = len(inp)
    re = r(inp)
    print(re)
    if inp == re :
        s ='It is a palindrome'
    else:
        s = "not palindrome"
    return s
#p()