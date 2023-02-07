class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = defaultdict(int)
        left, total, res= 0, 0, 0
        
        for r in range(len(fruits)):
            h[fruits[r]] += 1
            total += 1
            
            # when there are more than 2 fruits in hashmap
            # we will pop fruits until hash map is valid again
            while len(h) > 2:
                f = fruits[left]
                h[f] -= 1
                total -= 1
                left += 1
                
                if not h[f]:
                    h.pop(f)
            
            res = max(res, total)
        return res
        