class Solution:
    def average(self, salary: List[int]) -> float:
        mx, mn , s = salary[0], salary[0], 0
        for i in salary:
            s += i
            mx = max(mx, i)
            mn = min(mn, i)
        return (s - mx - mn) / float(len(salary) - 2)
        