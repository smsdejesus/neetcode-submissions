class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, ans = [], 0
        
        for op in operations:
            if op == "+":
                ans += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                ans += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif op == "C":
                ans -= stack.pop()
            else:
                ans += int(op)
                stack.append(int(op))
        return ans

