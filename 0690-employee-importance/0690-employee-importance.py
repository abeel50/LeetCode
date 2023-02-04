"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        h = {}
        
        for emp in employees:
            if emp.id not in h:
                h[emp.id] = emp
                
        res = h[id].importance
        q = deque(h[id].subordinates)
        
        while q:
            emp = q.popleft()
            res += h[emp].importance
            q.extend(h[emp].subordinates)
        return res
            
        