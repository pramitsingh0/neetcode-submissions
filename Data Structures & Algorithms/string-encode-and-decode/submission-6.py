class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        List of Strings -> String
        encode a list of string to a single string by prepending each word with len(word)#
        """
        res = ""
        for _str in strs:
            res += str(len(_str)) + "#" + _str
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
            j = i
            if s[i].isnumeric():
                while s[j] != "#":
                    j += 1
                word_length = int(s[i:j])
                word = s[j + 1 : j + 1 + word_length]
                i = j + word_length + 1
                res.append(word)
            else:
                i += 1
        return res
