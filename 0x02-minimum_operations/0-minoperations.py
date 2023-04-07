#!/usr/bin/python3
"""minimum operations"""

def minOperations(n):
"""function for the minimum operations"""
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
                dp[i] = min(dp[i], dp[i // j] + j)
        dp[i] = min(dp[i], dp[i - 1] + 1)
    return dp[n]
