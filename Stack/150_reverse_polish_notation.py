"""
    We use a stack to solve this problem. We iterate through the tokens and add the numbers to the stack.
    If the token is an operator, we pop the two numbers from the stack and perform the operation.
    We then push the result back onto the stack.
    If we finish the loop, we return the top of the stack.
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l+r)
                elif t == '-':
                    stack.append(l-r)
                elif t == '*':
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        
        return stack.pop()
        