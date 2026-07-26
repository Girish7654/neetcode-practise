class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        e={}
        f={}
        for i in s:
            if i in e:
                e[i]+=1
            else:
                e[i]=1

        for i in t:
            if i in f:
                f[i]+=1
            else:
                f[i]=1


        if len(s)!=len(t):
            return False

        if e==f:
            return True 
        else:
            return False