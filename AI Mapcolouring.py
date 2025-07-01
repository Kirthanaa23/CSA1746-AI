colors = ['Red', 'Green', 'Blue']
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
n = len(graph)
assign = [None] * n

def solve(i):
    if i == n: return True
    for color in colors:
        if all(assign[nei] != color for nei in graph[i]):
            assign[i] = color
            if solve(i + 1): return True
            assign[i] = None
    return False

if solve(0):
    print("Solution Exists: Following are the assigned colors")
    print(*assign)
else:
    print("No solution found")
