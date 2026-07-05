class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        bfs1 = deque()
        bfs2 = deque()
        bfs_pair = [bfs1, bfs2]

        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 2:
                    bfs_pair[0].append((i, j))

        minutes = 0
        while bfs_pair[minutes%2]:
            print(minutes)
            d1 = bfs_pair[minutes%2]
            d2 = bfs_pair[(1+minutes)%2]
            curr = d1.popleft()
            x, y = curr
            if (x-1) >= 0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                d2.append((x-1, y))
            if (x+1) < rl and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                d2.append((x+1, y))
            if (y-1) >= 0 and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                d2.append((x, y-1))
            if (y+1) < cl and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                d2.append((x, y+1))
            if not d1 and d2:
                minutes += 1
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1:
                    return -1
        return minutes