class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=[]
        for i in range(0,2):
            for i in nums:
                n.append(i)
        return n
