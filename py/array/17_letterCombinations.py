# -*- coding: utf-8 -*-
"""
作者：yuzihan
日期：2022年02月22日
"""
from typing import List


class Solution:
    """
    17. 电话号码的字母组合
    """
    def letterCombinations(self, digits: str) -> List[str]:
        # 思路：这是排列组合问题，直接上最通用的回溯算法（深度优先的特殊情况）。
        # 三步曲：递归函数，终止条件，递归调用。另外针对python语言的特点也有更简洁的解法
        # 1、 初始化及特殊处理
        if not digits:
            return []
        num = len(digits)
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if num == 1:
            return list(phoneMap[digits])
        # index = 0
        letters = '' # letters临时存放电话号码的字母组合元素
        res = []


        def backTrack(index: int):
            nonlocal letters
            if index == num:
                res.append(letters)
                return
            else:
                for c in phoneMap[digits[index]]:
                    letters += c
                    backTrack(index + 1)
                    letters = letters[: -1] # 退出当前一层之前删除当前元素

        backTrack(0)
        return res  # 不要忘了返回值


if __name__ == "__main__":
    solution = Solution()
    # print(solution.letterCombinations('23'))
    print(solution.letterCombinations('2'))
    # print(solution.letterCombinations(''))

