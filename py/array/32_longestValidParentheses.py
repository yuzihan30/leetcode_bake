class Solution:
    """
    32. 最长有效括号
    给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
    """
    def longestValidParentheses(self, s: str) -> int:
        # 思路： 利用栈结构处理，栈底始终保留最后一个没有匹配的右括号的索引
        # 1. 初始化和特殊处理
        if not s:
            return 0
        # 初始化栈底索引为-1，模拟初始未匹配的右括号的索引，方便后面找规律计算
        stack = [-1]
        # 初始化当前有效括号子串的长度，以及当前有效括号子串的最长长度
        length, max_length = 0, 0

        # 2. 遍历字符串，遇到左括号压栈，遇到右括号(如果栈长度大于1)出栈，并更新当前有效子串长度和最长长度
        for i, c in enumerate(s):
            if c == '(':
                # stack.append(c) # 易错点：压栈的是索引，不是元素
                stack.append(i)
            elif len(stack) == 1: # 栈底有个右括号索引，此时又遇到右括号
                stack.pop()
                stack.append(i)
                length = 0  # 容易遗漏
            else:  
                # length = i - stack[0]
                # 易错点：栈顶元素左括号出栈
                stack.pop()
                # length = i - stack[len(stack) - 1]
                length = i - stack[-1]
                max_length = max(max_length, length)
                # stack.pop()
                # stack.append(i)

        # 3. 返回结果值
        return max_length