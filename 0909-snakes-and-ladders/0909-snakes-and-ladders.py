class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # length of board
        n = len(board)
        #for labeling cells i,e. 1,2,3,4...
        labelCells = [None] * (n ** 2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                labelCells[label] = (row, column)
                label += 1
            # reversing colums cause it's  Boustrophedon style
            columns.reverse()
        
        dist = [-1] * (n * n + 1)
        
        #starting from cell 1
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = labelCells[next]
                destination = (board[row][column] if board[row][column] != -1 else next)
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        return dist[n * n]
        