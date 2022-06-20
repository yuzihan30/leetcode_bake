class Solution:
    """
    20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
    """
    def isValid(self, s: str) -> bool:
        # 思路：使用栈结构处理，遇到左括号压栈，遇到右括号出栈
        #  1、初始化
        stack = []
        # 关键点
        cache = { '(': ')',  '{': '}', '[': ']'}
        # 2、遍历所有字符
        for c in s:
            # 左括号的处理：压栈
            if c in cache:
                stack.append(c)
            # 右括号的处理，先出栈（出栈前看栈是否为空）
            elif not stack or cache[stack.pop()] != c:
                return False

        # return False if stack else True
        # 如果最后栈里没有剩余元素，则返回True
        return len(stack) == 0