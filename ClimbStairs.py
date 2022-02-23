"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

class ClimbStairs:
    number_of_ways = 0
    dp = {}

    def climbStairs(self, n: int) -> int:

        if n < 2:
            self.dp[n] = 1
        if n < 0 or n > 45:
            return 0

        if n in self.dp:
            return self.dp[n]
        if n >= 2:
            self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.dp[n]

    def bestSolution(self, n:int) -> int:
        one,two=1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one

stairs = 38

climbStairs = ClimbStairs()
print(climbStairs.bestSolution(38))
print(climbStairs.climbStairs(38))




key_value = {}

# Initializing value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

result = max(sorted (key_value.keys()))

print(result)