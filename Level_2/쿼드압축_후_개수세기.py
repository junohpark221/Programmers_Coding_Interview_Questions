def isSame(arr):
    zero=0
    one=0
    answer=0
    
    for row in arr:
        for num in row:
            if num==0:
                zero+=1
            else:
                one+=1
            if zero>0 and one>0:
                break
        if zero>0 and one>0:
            answer=-1
            break
            
    if answer!=-1:
        answer=0 if zero>0 else 1
        
    return answer

def solution(arr):
    answer = []
    sqSize=len(arr[0])
    isSameAns=isSame(arr)
    
    if isSameAns==0:
        answer=[1,0]
    elif isSameAns==1:
        answer=[0,1]
    else:
        sq1,sq2,sq3,sq4=[],[],[],[]
        for i in range(sqSize):
            if i<sqSize//2:
                sq1.append(arr[i][:sqSize//2])
                sq3.append(arr[i][sqSize//2:])
            else:
                sq2.append(arr[i][:sqSize//2])
                sq4.append(arr[i][sqSize//2:])
        sq1Ans,sq2Ans,sq3Ans,sq4Ans=solution(sq1),solution(sq2),solution(sq3),solution(sq4)
        answer.append(sq1Ans[0]+sq2Ans[0]+sq3Ans[0]+sq4Ans[0])
        answer.append(sq1Ans[1]+sq2Ans[1]+sq3Ans[1]+sq4Ans[1])
        
    return answer
