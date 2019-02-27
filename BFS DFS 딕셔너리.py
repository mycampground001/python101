def BFS(dict, v):
    queue = [v]
    visited = []
    layer = {}
    for i in range(1,V+1):
        layer.update({i:0})
    while queue:
        t = queue.pop(0)
        visited.append(t)
        for i in dict[t]:
            if i not in queue + visited:
                queue.append(i)
                layer[i] = layer[t] + 1
    return visited, layer


def DFS(dict, v):
    stack = [v]
    visited = []
    layer = {}
    for i in range(1,V+1):
        layer.update({i:0})
    while stack:
        v = stack.pop()
        visited.append(v)
        for i in dict[v]:
            if i not in stack + visited:
                stack.append(i)
                layer[i] = layer[v] + 1
    return visited, layer

V,E= 7, 8
mm = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
data = list(map(int,mm.split()))

samsung = {}
for i in range(1,V+1):
    samsung.update({i:[]})

for i in range(V+1):
    start = data[i*2]
    end = data[i*2+1]
    for key in range(1,V+1):
        if key == start: samsung[key].append(end)
        if key == end: samsung[key].append(start)

print(BFS(samsung,1))
print(DFS(samsung,1))