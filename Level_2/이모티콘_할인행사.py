from itertools import product

def howMuch(users, emoticons, dis_option):
    plus_user=0
    profit=0
    
    for user in users:
        spend=0
        for i, emoticon in enumerate(emoticons):
            if dis_option[i]>=user[0]:
                spend+=(((100-dis_option[i])*emoticon)//100)
            if spend>=user[1]:
                break
        if spend>=user[1]:
            plus_user+=1
        else:
            profit+=spend
            
    return plus_user, profit

def solution(users, emoticons):
    answer = []
    discount=[10, 20, 30, 40]
    dis_options=list(product(discount, repeat=len(emoticons)))
    most_user=0
    most_profit=0
    
    for dis_option in dis_options:
        plus_user, profit = howMuch(users, emoticons, dis_option)
        
        if plus_user>most_user:
            most_user=plus_user
            most_profit=profit
        elif plus_user==most_user:
            most_profit=max(most_profit, profit)
            
    return [most_user, most_profit]
