"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""

class Pow:

    pow_dict = {}

    def myPow(self, x: float, n: int) -> float:

        self.pow_dict.clear()
        return pow(x, n)

    def pow(self, x: float, n: int) -> float:
        if n < -0:
            return self.myPow(1 / x, n * -1)

        if n in self.pow_dict:
            return self.pow_dict[n]

        if n > 1:
            self.pow_dict[n] = x * self.myPow(x, n - 1)
            return self.pow_dict[n]

        if n == 1:
            return x

        if n == 0:
            return 1

    def efficientPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1 :
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

power = Pow()
print(power.myPow(2.1, 3))







