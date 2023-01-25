from itertools import permutations
import math

def isPrime(num_str):
    res=1
    num=int(num_str)
    
    if num<2:
        res=0
    else:
        num_sqrt=math.sqrt(num)
        for i in range(2, math.floor(num_sqrt)+1):
            if num%i==0:
                res=0
                break
                
    return res

def solution(numbers):
    answer = 0
    num_list=list(numbers)
    num_perm=[]
    used=[]
    
    for i in range(1, len(num_list)+1):
        num_perm+=list(permutations(num_list, i))

    for num in num_perm:
        num_str=''.join(s for s in num)
        if num[0]!='0' and num_str not in used:
            used.append(num_str)
            res=isPrime(num_str)
            if res==1:
                answer+=1        
                       
    return answer
