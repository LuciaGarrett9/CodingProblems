# Increment the large integer by one and return the resulting array of digits.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1

        while (i > -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
            i -= 1


        digits.insert(0,1)

        return digits