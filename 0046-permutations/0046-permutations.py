class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def dfs(path: List[int]) -> None:
          if len(path) == len(nums):
            ans.append(path.copy())
            return

          for i, num in enumerate(nums):
            if used[i]:
              continue
            used[i] = True
            path.append(num)
            dfs(path)
            path.pop()
            used[i] = False

        dfs([])
        return ans
#         res = []
        
#         if len(nums) == 1:
#             return [nums[:]]
#         print(res)

#         for i in range(len(nums)):
#             n = nums.pop(0)
#             print(nums)
#             perms = self.permute(nums)

#             for p in perms:
#                 perms.append(n)
#             res.extend(perms)
#             print(res)
#             nums.append(n)
#         return res

            
        