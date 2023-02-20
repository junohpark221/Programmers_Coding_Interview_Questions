def strToTime(time):
    result=36000*int(time[0])+3600*int(time[1])+600*int(time[3])+60*int(time[4])+10*int(time[6])+int(time[7])
    
    return result

def timeToStr(time):
    int_hour=time//3600
    tmp=time%3600
    int_minute=tmp//60
    int_sec=tmp%60
    
    hour=str(int_hour)
    minute=str(int_minute)
    sec=str(int_sec)
    
    if int_hour<10: hour="0"+hour
    if int_minute<10: minute="0"+minute
    if int_sec<10: sec="0"+sec
    
    return hour+":"+minute+":"+sec

def solution(play_time, adv_time, logs):
    answer = ''
    
    play_total_time=strToTime(play_time)
    adv_total_time=strToTime(adv_time)
    
    if play_total_time==adv_total_time:
        answer="00:00:00"
    else:
        timeline=[0 for _ in range(play_total_time+1)]

        for log in logs:
            start=strToTime(log[:8])
            end=strToTime(log[9:])
            
            timeline[start]+=1
            timeline[end]-=1
        
        for i in range(1, len(timeline)):
            timeline[i]=timeline[i-1]+timeline[i]
        
        start_time=0
        watch_time=sum(timeline[:adv_total_time])
        max_watch_time=watch_time
        for i in range(1, play_total_time-adv_total_time+1):
            watch_time-=timeline[i-1]
            watch_time+=timeline[i+adv_total_time-1]
            
            if watch_time>max_watch_time:
                max_watch_time=watch_time
                start_time=i
                
        answer=timeToStr(start_time)
            
    return answer
