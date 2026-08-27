class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        List of Strings -> String
        encode a list of string to a single string by prepending each word with len(word)#
        """
        res = ""
        for _str in strs:
            res += "#" + str(len(_str)) + _str
        return res

    def decode(self, s: str) -> list[str]:
        """
        String -> List of Strings
        decode the encoded string; if #is followed by a number then create a word of that many number of characters and add it to result array
        """
        res = []
        n = len(s)
        for i in range(n):
            if i < n - 1 and s[i] == "#" and s[i + 1].isnumeric():
                word_length = int(s[i + 1])
                res.append(s[i + 2 : i + word_length + 2])
                i += word_length + 2
        return res

