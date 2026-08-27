class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += str(len(word)) + '#' + word
        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_strings = []
        for i in range(len(s) - 1):
            if s[i].isdigit() and s[i + 1] == '#':
                j = i + 2
                temp_str = s[j:j + int(s[i])]
                decoded_strings.append(temp_str)
        return decoded_strings