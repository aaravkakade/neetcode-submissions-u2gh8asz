class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        nums.sort()


        def backtrack(index, path):
            if index == len(nums):
                result.add(tuple(path.copy()))
                return

            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)

        backtrack(0, [])
        result = [i for i in result]
        return result