def solution(bridge_length, weight, truck_weights):
    answer=0
    time=0
    on_the_bridge=[]
    on_the_bridge_weight=0
    this_truck=0
    
    while(len(truck_weights)>0):
        time+=1
        this_truck=truck_weights.pop(0)
        on_the_bridge.append([this_truck, time+bridge_length])
        on_the_bridge_weight+=this_truck
        if on_the_bridge_weight>weight:
            tmp_weight=0
            for truck in on_the_bridge:
                tmp_weight+=truck[0]
                if on_the_bridge_weight-tmp_weight<=weight:
                    time=truck[1]
                    on_the_bridge[-1][1]=time+bridge_length
                    break
        
        del_list=0          
        for done_truck in on_the_bridge:
            if done_truck[1]<=time:
                on_the_bridge_weight-=done_truck[0]
                del_list+=1
            else:
                break     
                
        on_the_bridge=on_the_bridge[del_list:]
        
    
    if len(on_the_bridge)==0:
        answer=time
    else:
        answer=on_the_bridge[-1][1]       
        
    return answer
