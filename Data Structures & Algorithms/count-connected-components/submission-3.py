class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {}
        for i in range(n):
            g[i] = []
        for edge in edges:
            a, b = edge
            g[a].append(b)
            g[b].append(a)
        counter = 0
        while g:
            dfs = [list(g)[0]]
            while dfs:
                curr = dfs.pop()
                if curr not in g:
                    continue
                for n in g[curr]:
                    dfs.append(n)
                g.pop(curr)
            counter += 1
        return counter

