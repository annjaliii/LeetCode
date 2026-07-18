class Solution(object):

    def permute(self, nums):
        ans = []  
        
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return ans

    