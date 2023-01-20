class Solution:
    def interpret(self, command: str) -> str:
        # h = {"G":"G" , "()": "o", "(al)":"al"}
        # command = command.replace("()", "o")
        # command = command.replace("(al)", "al")
        
        res, i = "", 0
        while i < len(command):
            c = command[i]
            if c == "G":
                res += "G"
                i += 1
            elif c == '(':
                lookAhead = i + 1
                if lookAhead < len(command) and command[lookAhead] == ")":
                    res += "o"
                    i = lookAhead + 1

                elif lookAhead < len(command) and command[lookAhead] == "a":
                    res += "al"
                    i += 4
                                
        return res
    
    
        
        