def solution(numbers):
    answer =''
    ans_list=[]
    for num in numbers:
        ans_list.append(str(num))
    ans_list.sort(reverse=True, key=lambda x:x*3)
    
    for ans in ans_list:
        answer+=ans

    return str(int(answer))
