class Solution:
    def calculate(self, s: str) -> int:
        # use stack to store all numbers
        stack = []
        preSign = '+'
        tempNum = 0
        for i in range(len(s)):
            if s[i].isdigit():
                tempNum = tempNum*10+int(s[i])
            if s[i] in "+-*/" or i == len(s)-1:
                if preSign == "+":
                    stack.append(tempNum)
                if preSign == '-':
                    stack.append(-tempNum)
                if preSign == '*':
                    last = stack.pop()
                    stack.append(last*tempNum)
                if preSign == '/':
                    last = stack.pop()
                    stack.append(int(last/tempNum))
                preSign = s[i]
                tempNum = 0
        return sum(stack)
            
        