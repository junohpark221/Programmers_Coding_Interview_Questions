def visit(ship, wolf, this_node, next_visit):
    global max_ship
    new_ship=ship
    new_wolf=wolf
    new_next_visit=next_visit.copy()

    if animal[this_node]==0:    new_ship+=1
    else:   new_wolf+=1
    
    new_next_visit+=tree_dict[this_node]
    
    if new_ship<=new_wolf or len(new_next_visit)==0:
        if new_ship>max_ship:   max_ship=new_ship
    else:
        for next_node in new_next_visit:
            this_next_visit=new_next_visit.copy()
            this_next_visit.remove(next_node)
            visit(new_ship, new_wolf, next_node, this_next_visit)
    

def solution(info, edges):
    global max_ship, tree_dict, animal
    max_ship=0
    tree_dict={}
    animal=info.copy()
    
    for i in range(len(info)):
        tree_dict[i]=[]
        
    for edge in edges:
        tree_dict[edge[0]].append(edge[1])
        
    visit(0, 0, 0, [])
    
    return max_ship
