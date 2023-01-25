from itertools import combinations

def solution(orders, course):
    dic = {}
    tmp_answer = []
    answer=[]
    orders_comb=[]
    
    for num in course:
        dic[num]={}
    
    for order in orders:
        res=[]

        for num in course:
            if num <= len(order):
                res+=list(combinations(sorted(order), num))

        orders_comb.append(res)
        
    for order_comb in orders_comb:
        for comb in order_comb:
            if comb in dic[len(comb)]:
                dic[len(comb)][comb]+=1
            else:
                dic[len(comb)][comb]=1
                
    for num in course:
        dic_list=list(dic[num].items())
        dic_list.sort(key=lambda x:x[1], reverse=True)
        
        times=2
        for element in dic_list:
            if element[1]>=times:
                tmp_answer.append(element[0])
                times=element[1]
            else:
                break     
    
    for element in tmp_answer:
        answer.append(''.join(str(s) for s in element))
        
    answer.sort()
        
    return answer
