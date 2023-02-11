class Solution:
    
    def solve(self, a, b, op):
        if op == "*": return a * b
        elif op == "/": return int(a / b)
        elif op == "+": return a + b
        else: return a - b
        
    def calculate(self, s: str) -> int:
        
        ops = {'-':1, '+':1, '/':2,'*':2 }
        valStack, opStack = [] , []
        i = 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            if c in ops:
                if len(opStack) == 0: 
                    opStack.append(c)
                else:
                    if ops[opStack[-1]] < ops[c]:
                        opStack.append(c)
                    else:
                        while len(opStack) > 0 and ops[opStack[-1]] >= ops[c]:
                            op = opStack.pop()
                            v2, v1 = valStack.pop(), valStack.pop()
                            valStack.append(self.solve(v1, v2, op))
                        opStack.append(c)
                        
            else:
                num = ""
                while i < len(s) and s[i].isnumeric():
                    num += s[i]
                    i += 1
                valStack.append(int(num))
                i -= 1
            i += 1
                
        while len(opStack) != 0:
            op = opStack.pop()
            v2, v1 = valStack.pop(), valStack.pop()
            valStack.append(self.solve(v1, v2, op))
        return valStack[0]
            