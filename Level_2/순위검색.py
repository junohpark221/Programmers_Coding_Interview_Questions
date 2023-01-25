def solution(infos, query):
    answer = []
    
    info_dict={}
    
    for lang in ['cpp', 'java', 'python', '-']:
        for job in ['frontend', 'backend', '-']:
            for career in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    info_dict[lang, job, career, food]=[]
    
    for info in infos:
        list_info=info.split()
        for lang in [list_info[0], '-']:
            for job in [list_info[1], '-']:
                for career in [list_info[2], '-']:
                    for food in [list_info[3], '-']:
                        info_dict[lang, job, career, food].append(int(list_info[4]))
    
    for key in info_dict.keys():
        info_dict[key].sort()
    
    for q in query:
        q_list_wAnd=q.split()
        q_list=[]
        this_q_answer=0
        
        for elem in q_list_wAnd:
            if elem!='and':    q_list.append(elem)
        
        q_score=int(q_list[4])
        score=info_dict[q_list[0], q_list[1], q_list[2], q_list[3]]
        
        l=len(score)
        low, high, cur=0, l-1, l
        
        while(low<=high):
            mid=(low+high)//2
            
            if score[mid]>=q_score:
                cur=mid
                high=mid-1
            else:
                low=mid+1
            
        answer.append(l-cur)

    return answer
