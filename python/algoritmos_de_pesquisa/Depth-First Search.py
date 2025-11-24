def Depth_First_Search_Rercursive(tree,node, visited = None):
    if visited is None:
        visited = set() 
    visited.add(node)
    print(node)
    for child in tree[node]:
        if child not in visited:
            Depth_First_Search_Rercursive(tree,child,visited)


def Depth_First_Search_Iterative(tree,start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(reversed(tree[node]))

# Define the decision tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}
# iniciando o depth first search em node A 
Depth_First_Search_Rercursive(tree,'A')
Depth_First_Search_Iterative(tree,'A')