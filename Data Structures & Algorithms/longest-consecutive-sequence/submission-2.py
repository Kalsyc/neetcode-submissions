class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dict_next = {i: i+1 for i in nums}
        seen = {}
        result = 1
        for key in dict_next.keys():
            if key in seen:
                continue
            next_key = dict_next[key]
            seen[key] = True
            curr = 1
            while next_key in dict_next:
                curr += 1
                seen[next_key] = True
                next_key = dict_next[next_key]
            result = max(result, curr)
        return result