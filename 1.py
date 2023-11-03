def solution(s):
    l=[]
    for i in range(1,len(s)+1):
        if(len(s) % i == 0):
            l.append(i)
    for j in l:
        if (s[0:j] * int(len(s)/j) == s):
            x = int(len(s)/j)
            break
    return(x)