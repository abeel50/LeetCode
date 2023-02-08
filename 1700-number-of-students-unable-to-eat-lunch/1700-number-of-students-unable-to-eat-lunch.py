class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        q = deque([*range(len(students))])
        eaten = 0
        circle = 0
        while q:
            s = q.popleft()
            if len(sandwiches) > 0 and students[s] == sandwiches[0]:
                sandwiches.pop(0)
                eaten += 1
                circle = 0
            else:
                q.append(s)
                circle += 1
            if circle == len(q):
                break
        return len(students) - eaten