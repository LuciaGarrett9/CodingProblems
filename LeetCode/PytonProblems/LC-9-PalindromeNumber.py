# Given an integer x
# return true if x is a palindrome
# false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        rev = 0

        while (n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10

        if (x == rev):
            return True
        return False