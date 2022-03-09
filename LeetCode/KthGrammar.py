"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
"""

"""
Thought process:
0
01
0110
01101001
0110100110010110

Each row's first half has the same digits as the previous row's
Each row's second half has the opposite digits as its first half
"""

class KthGrammar:
    def kthGrammar(self, n: int, k: int) -> int:
        # when row number is 1, we disregard k and return the only digit 0
        if n == 1:
            return 0

        # we need to know the number of digits in the nth row
        numberOfPositions = pow(2, n - 1)

        # if kth pos is in the first half of the row, the value will be the same as the kth position in the row n-1
        if k <= numberOfPositions / 2:
            return self.kthGrammar(n - 1, k)
        """
        if kth pos is in the second half of the row, its value will be the opposite to that of the position at 
        k-length/2, therefore, we instead look for the opposite value to the first-half position
        """
        if k > numberOfPositions / 2:
            return 1 - self.kthGrammar(n - 1, k - numberOfPositions / 2)



#Test
kthGrammar = KthGrammar()
row = 3
pos = 3
kthDigit = kthGrammar.kthGrammar(row, pos)
print(f'The value on row number {row} at position {pos} is {kthDigit}.')
