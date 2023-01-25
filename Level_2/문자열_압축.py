def findLength(s, unit):
    prev=''
    cnt=1
    answer_s=''
    for i in range(len(s)//unit):
        start=i*unit
        end=(i+1)*unit
        if s[start:end]==prev:
            cnt+=1
        else:
            if cnt==1:
                answer_s+=prev
            else:
                answer_s+=str(cnt)+prev
                cnt=1
            prev=s[start:end]
            
    if cnt==1:
        answer_s+=prev
    else:
        answer_s+=(str(cnt)+prev)
                
    if len(s)%unit!=0:
        answer_s+=s[len(s)-(len(s)%unit):]
    
    return len(answer_s)

def solution(s):
    answer = len(s)
    for unit in range(1, len(s)+1):
        tmp_answer=findLength(s, unit)
        if tmp_answer<answer:
            answer=tmp_answer
    return answer
