class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        dp = [0] * len(t)
        for i in reversed(range(len(t) - 1)):
            h = i + 1
            while True:
                if t[h] > t[i]:
                    dp[i] = h - i
                    break
                elif dp[h] != 0:
                    h += dp[h]
                else:
                    break
        return dp