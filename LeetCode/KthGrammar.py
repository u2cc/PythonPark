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


"""
This solution exploits the pattern that the first-half positions will have the same value as the row immediately above.
"""
class AlternateSolution:
    def kthGrammar(self, n: int, k: int) -> int:
        #exploit the fact that the first two rows have the same value for their respective first position
        if n < 3:
            return int('01'[k - 1])

        #flag to mark the number of times for value conversion between 0 and 1
        flag = 0
        #times to calculate the total length of the row
        times = 2 ** (n - 1)

        while n > 2:
            # if the position k is in the second half of the row
            if k > times // 2:
                #move position from k to the corresponding position in the first half
                k -= times // 2
                #mark value conversion once for the position change from 2nd half to 1st half of the row
                flag += 1
            #prepare for the n-1 row by calulating its length
            times //= 2
            n -= 1
        """
            in the end, if flag records even number of value conversion therefore self-cancelling-out, the value 
            will be the value from the deducted position in the standard '01' otherwise in reverse as '10'. 
            since python is 0-indexed but the quiz is 1-indexed, a k-1 operation is required. 
        """
        return '01'[k - 1] if flag % 2 == 0 else '10'[k - 1]

#Test
kthGrammar = KthGrammar()
row = 3
pos = 3
kthDigit = kthGrammar.kthGrammar(row, pos)
print(f'The value on row number {row} at position {pos} is {kthDigit}.')

print(int('0123'[3]))
