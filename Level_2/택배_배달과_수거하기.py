def solution(cap, n, deliveries, pickups):
    distance=0
    tot_cap=0
    
    suffix_D=[i for i in deliveries]
    suffix_P=[j for j in pickups]
    
    for index in range(n-2, -1, -1):
        suffix_D[index]=suffix_D[index+1]+suffix_D[index]
        suffix_P[index]=suffix_P[index+1]+suffix_P[index]
    
    for index in range(n-1, -1, -1):
        required=max(suffix_D[index], suffix_P[index])
        
        if required>tot_cap:
            new_trucks=(required-tot_cap)//cap + 1
            if (required-tot_cap)%cap==0:
                new_trucks-=1
            tot_cap+=new_trucks*cap
            distance+=new_trucks*(index+1)
    
    return distance*2
