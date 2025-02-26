# Given a string s consisting of words and spaces,
# return the length of the last word in the string.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.rstrip()
        s = s.lstrip()

        x = s.split(" ")

        length = len(x[-1])

        return (length)