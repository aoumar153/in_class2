
def word(s):
    c = 0
    for i in range(0, len(s)):
          
        # Check each char
        # is blank or not
        if s[i] == " " :
            c += 1
    print(c+1)
    return c+1

word("today is ugly")