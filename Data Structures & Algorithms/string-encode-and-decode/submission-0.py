class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string+=f"{len(string)}#{string}"

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        index=0
        length = 0
        while index<len(s):
            if s[index].isdigit():
                length= length*10 + int(s[index])
            if s[index]=="#":
                decoded_string=""
                for i in range(index+1,index+1+length):
                    decoded_string+=s[i]
                decoded_strs.append(decoded_string)
                index+=length
                length=0
            index+=1

        return decoded_strs
