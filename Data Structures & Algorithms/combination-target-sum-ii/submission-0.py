class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def dfs(i,cur,sum_):
            if target==sum_:
                res.append(cur.copy())
                return
            if target<sum_ or i>=len(candidates):
                return
            cur.append(candidates[i])
            dfs(i+1, cur, sum_+candidates[i])
            cur.pop()
            while  i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, cur,sum_)
        dfs(0,[],0)
        return res