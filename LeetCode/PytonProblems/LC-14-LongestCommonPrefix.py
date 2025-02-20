# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""
        length = len(strs[0])
        match = True

        for i in range(length):
            match = True
            testPrefix = strs[0][:i+1]
            for string in strs:
                if not (string.startswith(testPrefix)):
                    match = False
            if (match):
                prefix = testPrefix

        return(prefix)