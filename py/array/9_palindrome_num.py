class Solution:
    """
    9. 回文数
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
    """
    def isPalindrome(self, x: int) -> bool:
        # 思路：整数转字符串处理
        # # 1. 将原整数转为字符串
        # str_x = str(x)
        # # 2. 将字符串反转
        # str_x_reverse = str_x[::-1]
        # # 3. 判断字符串是否是回文，字符串是回文那么整数即是回文
        # if str_x == str_x_reverse:
        #     return True
        # return False

        # 优化 operator.eq(a, b)，a、b可以数字、字符串、列表 等价于"=="
        # return operator.eq(list(str(x)), list(str(x)[::-1]))
        # return operator.eq(str(x), str(x)[::-1])
        return str(x) == str(x)[::-1]