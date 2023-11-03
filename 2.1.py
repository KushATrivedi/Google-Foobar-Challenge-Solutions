def solution(s):
    rc = lc = x = y = 0
    for i in range(len(s)):
        if(s[i] == '<'):
            x = s[:i].count('>')
            lc = lc+x
        elif(s[i] == '>'):
            y = s[i:].count('<')
            rc = rc+y
    return(rc+lc)