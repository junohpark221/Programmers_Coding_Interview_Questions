from collections import deque

def findWinner(shots, info):
    diff=0
    for i in range(11):
        if shots[i]==0 and info[i]==0:
            continue
        elif shots[i]<=info[i]:
            diff-=(10-i)
        else:
            diff+=(10-i)
            
    return diff

def findResult(options):
    results=[]
    index=10
    shot_num=0
    
    for option in options:
        if len(results)==0:
            results.append(option)
            shot_num=option[index]
        else:
            if option[index]>shot_num:
                results=[option]
                shot_num=option[index]
            elif option[index]==shot_num:
                results.append(option)
                
    if len(results)!=1:
        index-=1
        while(len(results)!=1 or index>0):
            shot_num=0
            new_results=[]
            for option in results:
                if len(new_results)==0:
                    new_results.append(option)
                    shot_num=option[index]
                else:
                    if option[index]>shot_num:
                        new_results=[option]
                        shot_num=option[index]
                    elif option[index]==shot_num:
                        new_results.append(option)
            results=new_results
            index-=1
                
    return results[0]
            

def solution(n, info):
    options=deque([(0,[0 for _ in range(11)])])
    high_diff=0
    high_diff_options=[]
    
    while len(options)>0:
        index, shots=options.popleft()
        
        if index<=10:
            if sum(shots)+info[index]+1<=n:
                new_shots=shots.copy()
                new_shots[index]=info[index]+1
                options.append((index+1, new_shots))
            options.append((index+1, shots))
        else:
            if sum(shots)<n:
                shots[10]+=(n-sum(shots))
                options.append((index, shots))
            else:
                diff=findWinner(shots, info)
                if diff>high_diff:
                    high_diff=diff
                    high_diff_options=[shots]
                elif diff!=0 and diff==high_diff:
                    high_diff_options.append(shots)
    
    if len(high_diff_options)==0:
        return [-1]
    elif len(high_diff_options)==1:
        return high_diff_options[0]
    else:
        res=findResult(high_diff_options)
        return res
