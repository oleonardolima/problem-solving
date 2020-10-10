import collections
_input = list(input().split(" "))
while not (len(_input) == 2 and int(_input[0]) == 0 and int(_input[1]) == 0):
    if len(_input) == 2:
        num_nodes = int(_input[0])
        num_edges = int(_input[1])

        g_adj = collections.defaultdict(list)
        for _ in range(num_edges):
            _input = list(input().split(" "))
            g_adj[int(_input[0])].append([_input[1], _input[2]])
            g_adj[int(_input[1])].append([_input[0], _input[2]])

        print(g_adj)

    _input = list(input().split(" "))
    print(len(_input) == 2 and int(_input[0]) == 0 and int(_input[1]) == 0)
    print(_input)

def mst(g_adj):
    min_span_tree = collections.defaultdict(list)
    selected_nodes = [0 for node in g_adj]
    node_num = 