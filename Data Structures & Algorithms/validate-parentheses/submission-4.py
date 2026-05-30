class Solution:
    def isValid(self, s: str) -> bool:
        
        list = []
        dict = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i in dict: #checking if i is a closing bracket
                if list and list[-1] == dict[i]:
                    list.pop()
                else:
                    return False
            else: #if i is an opening bracket
                list.append(i)

        if not list:
            return True
        else:
            return False

        

