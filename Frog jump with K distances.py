def min_energy(heights, k):
    n = len(heights)
    dp = [0] * n
    
    for i in range(1, n):
        best = float('inf')
        for j in range(max(0, i - k), i):
            cost = dp[j] + abs(heights[i] - heights[j])
            best = min(best, cost)
        dp[i] = best
        
    return dp[-1]

print(min_energy([10, 5, 20, 0, 15], 2))   # 15
print(min_energy([15, 4, 1, 14, 15], 3))   # 2
