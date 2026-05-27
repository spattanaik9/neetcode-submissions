class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                val2, val1 = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(val1 + val2)
                elif t == '-':
                    stack.append(val1-val2)
                elif t == '*':
                    stack.append(val1 * val2)
                elif t == '/':
                    stack.append(int(val1/val2))
            else:
                stack.append(int(t))
            # print(stack)
        return stack[0]                        
                        
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# 22
        