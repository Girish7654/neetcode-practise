class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(min(strs))):
            for j in strs:
                if j[i]!=strs[0][i]:
                    return strs[0][:i]
        return min(strs)