def degree_centrality(graph_list, index):
    return len(graph_list[index])


def print_centrality(graph_list):
    for i in range(len(graph_list)):
        print(str(degree_centrality(graph_list, i)) + "\n")
    return None


def parse_input():
    first_line = input()
    first_line = first_line.split()
    number_nodes = int(first_line[0])
    number_edges = int(first_line[1])
    graph = [[] for j in range(number_nodes)]
    # initialization for graph
    for i in range(number_edges):
        my_line = lines[i + 1]
        my_line = my_line.split()
        my_line = [int(i) for i in my_line]
        if my_line[1] in graph[my_line[0]]:
            continue
        graph[my_line[0]].append([my_line[1], my_line[2]])
        graph[my_line[1]].append([my_line[0], my_line[2]])
        i = i + 1
    return graph


first_line = input()
first_line = first_line.split()
number_nodes = int(first_line[0])
number_edges = int(first_line[1])
graph = [[] for j in range(number_nodes)]

for i in range(number_edges):
    my_line = input()
    my_line = my_line.split()
    my_line = [int(i) for i in (my_line)]
    if my_line[1] in graph[my_line[0]]:
        continue
    graph[my_line[0]].append([my_line[1], my_line[2]])
    graph[my_line[1]].append([my_line[0], my_line[2]])
    i = i + 1

print_centrality(graph)