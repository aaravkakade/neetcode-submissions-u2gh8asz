class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        [2,20,4,10,3,4,5]
        1. is this the start of a sequence
        2. increment length while num + 1 in set
        3. find max of local var and current seq
        '''
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1

                longest = max(longest, length)

        return longest

        




