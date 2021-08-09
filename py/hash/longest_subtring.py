'''
无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
审题：
1、子串是连续的，区别于子序列
2、无重复字符
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. 定义返回的字符串最大长度
        max_len = 0
        # 2. 初始化慢指针
        low = 0
        # 3. 初始化字典，用于存储上次出现的字符及索引，须及时更新重复字符索引
        last_occurence = {}
        # 4. 遍历字符串中的字符和索引
        # for idx, single_char in enumerate(str):
        for idx, single_char in enumerate(s):
            # 5. 重复出现的判断 易错点：python中的逻辑与、按位与其他语言的区别
            if single_char in last_occurence and last_occurence[single_char] >= low:
                # 6. 更新慢指针（左指针）
                low = last_occurence[single_char] + 1
                # 7. 更新子串最大长度 遇到重复字符才更新一次 这里更新会有问题，
                # 如果一直没有重复的，就无法返回最大长度
                # max_len = max(max_len, idx - low)
                # 8. 更新上次重复字符出现的索引
                last_occurence[single_char] = idx
            else:
                last_occurence[single_char] = idx
                # 这里返回最大长度，虽然有重复计算，但准确
                max_len = max(max_len, idx - low + 1)

        return max_len
                

