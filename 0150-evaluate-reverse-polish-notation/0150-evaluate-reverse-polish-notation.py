class Solution:
    def evalRPN(self, tokens: List[str]) -> int: #["4","13","5","/","+"]
        if not tokens: return []
            
        stack = [] #[6]
        
        for token in tokens: #"+"
            if token == "+":
                num2 = stack.pop() # 4
                num1 = stack.pop() # 2
                stack.append(num1 + num2)
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token == "/":
                num2 = stack.pop() #5
                num1 = stack.pop() # 13
                stack.append(int(num1 / num2)) # 2
            else:
                stack.append(int(token))
        
        return stack[0]
    
    
    #Notes:
#         - if not tokens: return []
        
#         - use a stack
#         - set up stack -> []
        
#         - for loop going over all of the tokens
#             - check to see if the token is a num or operator
#                 - if it is a number
#                     - append that to stack
#                 - if not a number
#                     - pop the last two elements of the stack
#                     - call the operator on it
#                     - append new num to the stack
                    
#         - return stack at 0 index