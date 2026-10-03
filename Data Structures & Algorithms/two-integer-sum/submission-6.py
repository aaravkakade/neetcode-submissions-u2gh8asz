class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

    # we can store the nums in a hashmap, with the val as the index
    # as we iterate through the array, check if target - currnum in hashmap
    # if it is then we return its indices

        seen = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in seen:
                return [seen[complement], i]

            seen[n] = i

        

       
        
            
            
