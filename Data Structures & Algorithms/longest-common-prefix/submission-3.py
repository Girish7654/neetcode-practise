class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            for j in strs:
                if j[i] != strs[0][i]:
                    return strs[0][:i]

        return shortest