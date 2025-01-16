class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = strs[0]
        for i in range(1, len(strs)):
            longest_common_prefix = ""
            j = 0
            while j < len(strs[i]) and j < len(strs[i - 1]):
                if strs[i][j] != strs[i - 1][j]:
                    break
                longest_common_prefix += strs[i][j]
                j += 1
            if len(longest_common_prefix) < len(result):
                result = longest_common_prefix
        return result
