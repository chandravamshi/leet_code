
# https://www.lintcode.com/problem/659/

# 659 · Encode and Decode Strings

'''

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        return ''.join(map(lambda  s : f"{len(s)}#{s}",strs))

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0
        while i < len(str):
            j = i
            while j !='#':
                j +=1
            length = len(str[i:j])
            i = j + 1
            j = i + length
            res.append(str[i:j])
            i = j
