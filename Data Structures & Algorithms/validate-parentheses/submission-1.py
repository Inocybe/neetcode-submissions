class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        opened = []
        openers = "[{("

        for char in s:
            if char in openers:
                opened.append(char)
            else:
                if not opened:
                    return False
                if opened[len(opened) - 1] != self.getOpposite(char):
                    return False
                
                opened.pop(len(opened) - 1)
        
        if not opened:
            return True
        
        return False

    


    def getOpposite(self, char: str) -> str:
        match char:
            case "(":
                return ")"
            case ")":
                return "("
            case "{":
                return "}"
            case "}":
                return "{"
            case "[":
                return "]"
            case "]":
                return "["
            case _:
                return ""