class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rl = len(grid)
        cl = len(grid[0])
        bfs = deque()
        # def dis(i, j):

        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 0:
                    bfs.append((i, j))
        while bfs:
            curr = bfs.popleft()
            x, y = curr
            if (x-1) >= 0 and grid[x-1][y] == INF:
                grid[x-1][y] = 1 + grid[x][y]
                bfs.append((x-1, y))
            if (x+1) < rl and grid[x+1][y] == INF:
                grid[x+1][y] = 1 + grid[x][y]
                bfs.append((x+1, y))
            if (y-1) >= 0 and grid[x][y-1] == INF:
                grid[x][y-1] = 1 + grid[x][y]
                bfs.append((x, y-1))
            if (y+1) < cl and grid[x][y+1] == INF:
                grid[x][y+1] = 1 + grid[x][y]
                bfs.append((x, y+1))

                    # bfs = deque([(i, j)])
                    # trav = set()
                    # trav.add((i, j))
                    # while bfs:
                    #     x, y = bfs.popleft()
                    #     ds = [0, 1], [0, -1], [1, 0], [-1, 0]
                    #     for d in ds:
                    #         d1, d2 = d
                    #         if (x+d1, y+d2) not in trav:
                    #             bfs.append((x+d1, y+d2))
                    #             trav.add((x+d1, y+d2))

                            
