class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(index, path):
            #base case
            if index == len(nums):
                result.append(path.copy())
                return

            #include num
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            #skip num
            backtrack(index + 1, path)
        
        backtrack(0, [])

        return result

