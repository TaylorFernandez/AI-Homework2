import astar_algo
import csv

def load_graph_and_heuristics(edge_filename, heuristic_filename):
    # Load edge weights
    graph = {}
    with open(edge_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = next(reader)  # Skip the header row
        for row in reader:
            from_node = int(row['From'])
            to_node = int(row['To'])
            weight = float(row['Weight'])

            if from_node not in graph:
                graph[from_node] = {}
            graph[from_node][to_node] = weight

    # Load heuristics
    heuristics = {}
    with open(heuristic_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = next(reader)  # Skip the header row
        for row in reader:
            node_id_str = row['']
            if node_id_str:
                node_id = float(node_id_str)
                heuristics[node_id] = float(row['h = (min edge cost from start node +min edge cost from end node)/2'])

    return graph, heuristics

if __name__ == '__main__':
    edge_file_name = input("Please enter the edge weight file name and extension:")
    print("Loading File...")
    h_file_name = input("Please enter the heuristic file name and extension:")
    print("Loading File...")
    graph, heuristics = load_graph_and_heuristics(edge_file_name, h_file_name)

    start_node = int(input("Start Node (1 - 200):"))
    end_node = int(input("End Node (1 - 200):"))

    path = astar_algo.astar(graph, heuristics, start_node, end_node)

    if path:
        print(f"Minimum cost path from {start_node} to {end_node}: {path}")
    else:
        print(f"No path found from {start_node} to {end_node}")
