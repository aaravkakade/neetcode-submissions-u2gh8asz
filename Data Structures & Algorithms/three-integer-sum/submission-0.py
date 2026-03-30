class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        [-1,0,1,2,-1,-4]

        '''
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    res.add(tuple((nums[i], nums[l], nums[r])))
                    l += 1 
                    r -= 1


        return [list(i) for i in res]


