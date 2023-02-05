def findClosedNode(visited, distance, n):
    node=-1
    small_dist=max(distance)+1
    unlinked=[]
    
    for i in range(n):
        if visited[i]==0:
            if distance[i]==-1:
                unlinked.append(i)
            elif distance[i]<small_dist:
                node=i
                small_dist=distance[i]
                
    if node!=-1:
        return node
    else:
        if len(unlinked)==0:    return -1
        else:   return unlinked[0]

def dijkstra_full(start, n):
    distance=[-1 for _ in range(n)]
    visited=[0 for _ in range(n)]
    distance[start-1]=0
    visited[start-1]=1
    
    this_visit=start-1
    
    for _ in range(n-1):
        if this_visit!=-1:
            for i, route in enumerate(routes[this_visit]):
                if distance[this_visit]!=-1 and route!=-1:
                    if distance[i]==-1:
                        if route!=-1:   distance[i]=distance[this_visit]+route
                        else:   distance[i]=distance[this_visit]
                    else:
                        if route!=-1:
                            distance[i]=min(distance[i], distance[this_visit]+route)
                        
        this_visit=findClosedNode(visited, distance, n)
        visited[this_visit]=1

    return distance  
    
def dijkstra_res(start, end, n):
    if start==end:
        return 0
    
    distance=[-1 for _ in range(n)]
    visited=[0 for _ in range(n)]
    distance[start-1]=0
    visited[start-1]=1
    
    this_visit=start-1
    
    for _ in range(n-1):
        if this_visit!=-1:
            for i, route in enumerate(routes[this_visit]):
                if distance[this_visit]!=-1 and route!=-1:
                    if distance[i]==-1:
                        if route!=-1:   distance[i]=distance[this_visit]+route
                        else:   distance[i]=distance[this_visit]
                    else:
                        if route!=-1:
                            distance[i]=min(distance[i], distance[this_visit]+route)
        
        if visited[end-1]==1:
            break
        
        this_visit=findClosedNode(visited, distance, n)
        visited[this_visit]=1
                
    return distance[end-1]    

def solution(n, s, a, b, fares):
    answer = -1
    toADis=[-1 for _ in range(n)]
    toBDis=[-1 for _ in range(n)]
    
    global routes
    routes = [[-1 for _ in range(n)] for _ in range(n)]
    
    for fare in fares:
        routes[fare[0]-1][fare[1]-1]=fare[2]
        routes[fare[1]-1][fare[0]-1]=fare[2]

    fromS=dijkstra_full(s, n)

    for i in range(1, n+1):
        toADis[i-1]=dijkstra_res(i, a, n)
        toBDis[i-1]=dijkstra_res(i, b, n)
    
    for i in range(1, n+1):
        if fromS[i-1]!=-1 and toADis[i-1]!=-1 and toBDis[i-1]!=-1:
            this_dis=fromS[i-1]+toADis[i-1]+toBDis[i-1]
            if answer==-1:  answer=this_dis
            else:   answer=min(answer, this_dis)
        
    return answer
