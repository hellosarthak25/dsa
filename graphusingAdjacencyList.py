n, m = map(int, input().split())

adj = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n+1):
    print(i, ":", *adj[i])