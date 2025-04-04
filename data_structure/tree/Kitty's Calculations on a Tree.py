import sys
from collections import deque

MOD = 10 ** 9 + 7
#TODO: 提高效率

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, q = int(input[ptr]), int(input[ptr + 1])
    ptr += 2

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(input[ptr])
        v = int(input[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    # BFS to compute parent and depth
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    q_bfs = deque()
    root = 1
    q_bfs.append(root)
    visited[root] = True
    parent[root] = 0
    depth[root] = 0

    while q_bfs:
        u = q_bfs.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q_bfs.append(v)

    # Precompute binary lifting table
    LOG = 20  # Sufficient for up to 2^20 nodes
    jump = [[0] * LOG for _ in range(n + 1)]
    for i in range(1, n + 1):
        jump[i][0] = parent[i]
    for k in range(1, LOG):
        for i in range(1, n + 1):
            if jump[i][k - 1] != 0:
                jump[i][k] = jump[jump[i][k - 1]][k - 1]
            else:
                jump[i][k] = 0

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # Bring u to the depth of v
        for k in range(LOG - 1, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:
                u = jump[u][k]
        if u == v:
            return u
        # Now find the LCA
        for k in range(LOG - 1, -1, -1):
            if jump[u][k] != 0 and jump[u][k] != jump[v][k]:
                u = jump[u][k]
                v = jump[v][k]
        return parent[u]

    def get_distance(u, v):
        ancestor = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[ancestor]

    # Process queries
    results = []
    for _ in range(q):
        k = int(input[ptr])
        ptr += 1
        nodes = list(map(int, input[ptr:ptr + k]))
        ptr += k

        total = 0
        # Iterate over all pairs
        for i in range(k):
            u = nodes[i]
            for j in range(i + 1, k):
                v = nodes[j]
                dist = get_distance(u, v)
                total = (total + u * v * dist) % MOD
        results.append(total % MOD)

    sys.stdout.write('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()