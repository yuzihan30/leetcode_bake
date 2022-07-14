class Solution:
    """
    58. 最后一个单词的长度
    给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
    """
    def lengthOfLastWord(self, s: str) -> int:
        # 思路：先裁剪字符串两端空格，然后将字符串转为数组，求数组中最后一个字符串的长度
        # 1. 初始化及特殊处理
        if not s:
            return 0
        # 2. 去除前后空格，转数组
        helper_s = s.strip()
        helper_list = helper_s.split(' ')

        # 3. 返回结果值
        return len(helper_list.pop())