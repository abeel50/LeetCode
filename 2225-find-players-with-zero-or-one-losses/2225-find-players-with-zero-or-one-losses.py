from sortedcontainers import SortedDict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        #0 index win, 1 index loss
        players = SortedDict()
        
        for w, l in matches:
            if w not in players:
                players[w] = [1,0]
            else:
                wins, loss = players[w]
                players[w] = [wins + 1, loss]
            if l not in players:
                players[l] = [0,1]
            else:
                wins, loss = players[l]
                players[l] = [wins, loss + 1]
            
            
        return [[p for  p,v in players.items() if v[1] == 0], [p for  p,v in players.items() if v[1] == 1]]
        