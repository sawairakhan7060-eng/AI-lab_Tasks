graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":[],
    "F":["G"],
    "G":[]
}
stack=[]
def dls (node,goal,limit):  
    stack.append((node, 0, [node]))
    Cutoff=False
    while stack:
        temp,depth,path = stack.pop()  
        if temp == goal:
             return" Found",path
        if depth < limit:
            Cutoff=True
            continue

        for child in graph[temp]:
                stack.append((child, depth+1, path+[child]))
    if Cutoff:
       return "CUTOFF", None
    return "FAILURE", None
for limit in [1,2,3,4]:
    status, path = dls("A", "G", limit)
    print("Limit:", limit)
    print("Status:", status)
    print("Path:", path)
    print("Limits attempted:", [limit])
    print()
    