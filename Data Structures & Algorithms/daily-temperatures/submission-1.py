class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            # For each element that you see bigger than previous top, pop and update the days
            # Every time you encounter a higher temperature compared to the previous day, 
            # we update until we can no longer find something higher.
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

"""
[30, 38, 30, 36, 35, 40, 28]
[1,4,1,2,1,0,0]
"""