import collections
_input = list(input().split(" "))
#print(_input)
num_pc = int(_input[0])
otvio_pc = int(_input[1])

g_adj = collections.defaultdict(list)
for line in range(num_pc - 1):
    _input = list(input().split(" "))
    g_adj[int(_input[0])].append(int(_input[1]))
    g_adj[int(_input[1])].append(int(_input[0]))
    #print(g_adj)

max_depth = 0

queue = collections.deque()
queue.append(otvio_pc)

visited = set()
visited.add(otvio_pc)

while queue:
    for level in range(len(queue)):
        node = queue.popleft()
        for adj in g_adj[node]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)
    max_depth += 1
    #print(queue)
    #print(visited)


print(max_depth)