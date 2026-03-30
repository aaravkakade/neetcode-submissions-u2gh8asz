class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        [-1,0,2,4,6,8]
         0    m     5

        '''

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1