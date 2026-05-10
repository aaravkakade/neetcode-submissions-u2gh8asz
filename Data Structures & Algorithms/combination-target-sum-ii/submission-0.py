class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []

        def backtrack(index, path):
            if sum(path) == target:
                result.append(path.copy())
                return
            
            if sum(path) > target or index == len(candidates):
                return

            path.append(candidates[index])
            backtrack(index + 1, path)
            path.pop()

            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                index += 1

            backtrack(index + 1, path)

        backtrack(0, [])
        return result