def tree_by_levels(node):
    if not isinstance(node,Node):
        return []
    end=[]
    turn=[node]
    cur=0
    while len(turn)>cur:
        end.append(turn[cur].value)
        if isinstance(turn[cur],Node) and turn[cur].left:
            turn.append(turn[cur].left)
        if isinstance(turn[cur],Node) and turn[cur].right:
            turn.append(turn[cur].right)
        cur+=1
        if cur>=len(turn):
            break
    return end
