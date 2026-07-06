class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s = [0]
        ans = [0] * len(t)
        print(t)
        for i in range(1, len(t)):
            while s and t[i] > t[s[-1]]:
                cd = s.pop()
                ans[cd] = i - cd
            s.append(i)
        return ans