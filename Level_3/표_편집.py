def solution(n, k, cmd):
    answer=''
    answerDict={}
    answerList=['X' for _ in range(n)]
    cList=[]
    start=0
    location=k
    
    for i in range(n):
        if i==0:    answerDict[i]=[None, i, i+1]
        elif i==n-1:    answerDict[i]=[i-1, i, None]
        else:   answerDict[i]=[i-1, i, i+1]
    
    for op in cmd:
        opList=list(op)
        
        if opList[0]=='U':
            pos, moveStr=op.split()
            move=int(moveStr)
            for _ in range(move):
                tmp=answerDict[location][0]
                if tmp!=None:   location=tmp
            
        elif opList[0]=='D':
            pos, moveStr=op.split()
            move=int(moveStr)
            for _ in range(move):
                tmp=answerDict[location][2]
                if tmp!=None:   location=tmp
            
        elif opList[0]=='C':
            cList.append(location)
            
            prev=answerDict[location][0]
            after=answerDict[location][2]
            
            if prev!=None:  answerDict[prev][2]=after
            else:   start=after

            if after!=None:
                answerDict[after][0]=prev
                location=after
            else:   location=prev
            
        elif opList[0]=='Z':
            index=cList.pop()
            
            prev=answerDict[index][0]
            after=answerDict[index][2]
            
            if prev!=None:  answerDict[prev][2]=index
            if after!=None: answerDict[after][0]=index
            
            if index<start: start=index
    
    this=start
    after=start
    while after!=None:
        after=answerDict[this][2]
        answerList[this]='O'
        this=after
        
    answer=''.join(s for s in answerList)
        
    return answer
