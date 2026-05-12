class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(closedP, openP, path):
            if closedP == openP == n:
                result.append("".join(path))
                return

            if openP < n:
                path.append("(")
                backtrack(closedP, openP + 1, path)
                path.pop()

            if closedP < openP:
                path.append(")")
                backtrack(closedP + 1, openP, path)
                path.pop()

        backtrack(0, 0, [])
        return result

