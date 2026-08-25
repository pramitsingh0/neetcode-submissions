class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        List of Strings -> String
        encode a list of string to a single string by prepending each word with len(word)#
        """
        res = ""
        for s in strs:
            res += str( len(s) ) + "#" + s
        return res


    def decode(self, s: str) -> list[str]:
        """
        String -> List of Strings
        decode the encoded string; if #is followed by a number then create a word of that many number of characters and add it to result array
        """
        res = []
        n = len(s)
        i = 0
        while i < n:
            if s[i].isnumeric():
                j = i
                while s[j] != "#" and j < n:
                    j += 1
                print("i: ", i)
                print("j: ", j)
                word_len = s[i:j]
                word_len = int(word_len)
                print("word len: ", word_len)
                word = s[j + 1: j + 1 + word_len]
                i = j + 1 + word_len
                print("i after: ", i)
                res.append(word)
        return res
