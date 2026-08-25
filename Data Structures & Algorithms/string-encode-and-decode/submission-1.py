class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i
            if s[i].isnumeric():
                while s[j] != "#":
                    j += 1
                length = int(s[i:j])
                i = j + 1
                j = i + length
                decoded_strings.append(s[i:j])
                i = j
            else:
                i += 1
        return decoded_strings
