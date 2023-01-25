def solution(places):
    answer = []
    for room in places:
        roomAns=1
        for col, row in enumerate(room):
            for i in range(5):
                if row[i]=='P':
                    barriers=[1,1,1,1]
                    if col-1>=0:
                        if room[col-1][i]=='P':
                            roomAns=0
                            break
                        elif room[col-1][i]!='X':  barriers[0]=0
                    if i+1<5:
                        if row[i+1]=='P':
                            roomAns=0
                            break
                        elif row[i+1]!='X': barriers[1]=0
                    if col+1<5:
                        if room[col+1][i]=='P':
                            roomAns=0
                            break
                        elif room[col+1][i]!='X':   barriers[2]=0
                    if i-1>=0:
                        if row[i-1]=='P':
                            roomAns=0
                            break
                        elif row[i-1]!='X':    barriers[3]=0
                        
                    if barriers[0]==0:
                        if col-2>=0 and room[col-2][i]=='P':
                            roomAns=0
                            break
                    if barriers[0]==0 or barriers[1]==0:
                        if (col-1>=0 and i+1<5) and room[col-1][i+1]=='P':
                            roomAns=0
                            break
                    if barriers[1]==0:
                        if i+2<5 and room[col][i+2]=='P':
                            roomAns=0
                            break
                    if barriers[1]==0 or barriers[2]==0:
                        if (col+1<5 and i+1<5) and room[col+1][i+1]=='P':
                            print(barriers)
                            roomAns=0
                            break
                    if barriers[2]==0:
                        if col+2<5 and room[col+2][i]=='P':
                            roomAns=0
                            break
                    if barriers[2]==0 or barriers[3]==0:
                        if (col+1<5 and i-1>=0) and room[col+1][i-1]=='P':
                            roomAns=0
                            break
                    if barriers[3]==0:
                        if i-2>=0 and room[col][i-2]=='P':
                            roomAns=0
                            break        
                    if barriers[3]==0 or barriers[0]==0:
                        if (col-1>=0 and i-1>=0) and room[col-1][i-1]=='P':
                            roomAns=0
                            break
                            
            if roomAns==0:
                break
            
        answer.append(roomAns)
                        
    return answer
