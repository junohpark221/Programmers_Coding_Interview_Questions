def equalString(p):
    x=0
    index=0
    for char in p:
        index+=1
        if char=='(':  x+=1
        else:   x-=1
        
        if x==0:
            break
    
    return p[:index], p[index:]
    
def correctString(p):
    res=True
    x=0
    
    for char in p:
        if x<0:
            res=False
            break
            
        if char=='(':   x+=1
        else:   x-=1
    
    return res

def solution(p):
    answer = ''
    if len(p)==0:
        return p
    elif correctString(p):
        return p
    else:
        u, v = equalString(p)

        if correctString(u):
            answer=u+solution(v)
        else:
            new_u=u[1:len(u)-1]
            answer='('+solution(v)+')'
            for char in new_u:
                if char=='(':   answer+=')'
                else:   answer+='('
        return answer
