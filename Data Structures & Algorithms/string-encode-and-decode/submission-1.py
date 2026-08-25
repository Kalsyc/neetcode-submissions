class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for word in strs:
            if word == "":
                result += "E"
            else:
                result += ",".join(map(lambda x: str(ord(x)), word))
            result += "|"
        result = result[:-1]
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        split_s = s.split("|")
        for encoded_word in split_s:
            if encoded_word == "E":
                result.append("")
            else:
                result.append("".join(map(lambda x: chr(int(x)), encoded_word.split(",")))) 
        return result
