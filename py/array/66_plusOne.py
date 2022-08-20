class Solution:
    """
    66. 加一
    给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        # 思路：区分最后一位是小于9还是等于9，小于9直接加1，等于9则变0后进位加1；当每位都是9的情况，每位变零后头部需要插入1
        # 1. 初始化
        n = len(digits)

        # 2. 反向遍历
        for i in range(n-1, -1, -1):
            # 2.1 当前位小于9的情况
            if digits[i] < 9:
                # 涵盖了进位加1和最后一位加1两种情况
                digits[i] += 1
                break
            # 2.2 当前位为9的情况
            else:
                # 2.2.1 9变0
                digits[i] = 0
                # 2.2.2 如果是首位，首位前插入1
                if i == 0:
                    digits.insert(0, 1)
                    break

        # 3. 返回结果值
        return digits



