from itertools import combinations

def checkCandidateKey(relation, candidate):
    answer=True
    result=[]
    
    for info in relation:
        cand_info=[]
        
        for index in candidate:
            cand_info.append(info[index])
            
        if cand_info in result:
            answer=False
            break
        else:
            result.append(cand_info)
            
    return answer

def solution(relation):
    answer=[]
    elements=len(relation[0])
    candidates=[[i for i in range(elements)]]
    
    while(True):
        new_candidates=[]
        end=False
        
        for candidate in candidates:
            targets=list(combinations(candidate, len(candidate)-1))
            true_list=[]
            true_num=0
            false_num=0
            
            for target in targets:
                if len(target)==1:
                    end=True
                    
                if checkCandidateKey(relation, target):
                    if list(target) not in true_list:
                        true_list.append(list(target))
                        true_num+=1
                else:
                    false_num+=1
            
            if true_num==0 and false_num!=0 and (candidate not in answer):
                answer.append(candidate)
            elif true_num!=0:
                for element in true_list:
                    if element not in new_candidates:
                        new_candidates.append(element)
            
        candidates=new_candidates
        
        if end==True or len(candidates)==0:
            break
    
    answer+=candidates

    return len(answer)
