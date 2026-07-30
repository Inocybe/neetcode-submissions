import operator

operator_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in operator_map.keys():
                temp = int(token)
                stack.append(temp)
                continue
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                func = operator_map.get(token)
                stack.append(int(func(num2, num1)))
        
        return stack.pop()