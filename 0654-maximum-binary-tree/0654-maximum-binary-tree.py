# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def helper(nums):
            if len(nums) == 0: return None
            if len(nums) == 1: return TreeNode(nums[0])
            else:
                maxIndex = nums.index(max(nums))
                head = TreeNode(nums[maxIndex])
                head.left = helper(nums[:maxIndex])
                head.right = helper(nums[maxIndex+1:])
                return head
     
        return helper(nums)