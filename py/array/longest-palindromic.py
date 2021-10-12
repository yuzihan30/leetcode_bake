'''
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
注意点：
a: 子串是连续字符，子序列是字符集的子集
b: 特殊处理，单个字符是回文子串，两个字符必须相同才是回文字符串，这样才对称
同理，三个字符中两端的两个字符相同才是回文子串
动态规划思路：（思路类似于解题步骤的概念）
a: 将任意两个字符之间构成的闭区间内是否是构成回文子串问题，转化为二维数组填充布尔值的问题
b: 二维数组可看作是一个对称矩阵，对称轴上对应的s_arr[i][i]值填充为True
c: s_arr[i][j]的值取决于s_arr[i+1][j-1]的值，及s[i]、s[j]是否相等
d: 记录回文子串的起始索引start_index, 和最大长度max_len，这样可以切片截断回文子串
s[start_index, start_index+max_len]，注意切片含左不含右
题型分类：字符串类的问题可以归类到数组分类问题里
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. 处理特殊情况，size < 2
        size = len(s)
        if size < 2:
            return s
        
        # 定义回文子串的开始索引及最大长度 易错点：max_len初始化为1而不是0
        start_index, max_len = 0, 1

        # 2. 初始化二位数组
        s_arr = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            s_arr[i][i] = True

        # 3. 按列遍历，列的话索引为j 易错点：应从第2列开始遍历
        for j in range(1, size):
            # 列遍历只需要遍历主对角线以上的元素，即满足i > j，列从下往上遍历
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 2:
                        s_arr[i][j] = True
                    else: 
                        # 易错点：左下方的元素对应的索引应是列索引减1，行索引加1
                        s_arr[i][j] = s_arr[i+1][j-1]
                else:
                    s_arr[i][j] = False
                # 更新起始索引及最大长度
                if s_arr[i][j] and j - i + 1 > max_len:
                    start_index = i
                    max_len = j - i + 1 
        
        # 4. 返回最长回文字符串
        return s[start_index: start_index+max_len]

if __name__ == '__main__':
  solution = Solution()
  return_value = solution.longestPalindrome('ba')
  print(return_value)


"""
中心扩散法
"""

  class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        
        # 易错点2
        # 定义并初始化最长子串及其长度
        longest_palindrome = s[0]
        max_len = 1

        for i in range(size):
            odd_palindrome, odd_len = self.center_spread(s, size, i, i + 1)
            even_palindrome, even_len = self.center_spread(s, size, i, i)
            longer_palindrome = odd_palindrome if odd_len > even_len else even_palindrome
            if len(longer_palindrome) > max_len:
                max_len = len(longer_palindrome)
                longest_palindrome = longer_palindrome
            
        return longest_palindrome

    # size作为入参的好处，循环调用时只需要在外部计算一次，提高了效率
    def center_spread(self, s: str, size, left, right):
        # 易错点1
        i = left
        j = right
        # py中取字符串中的字符，使用索引即可
        while i >= 0 and j < size and s[i] == s[j]:
            # 易错点3 Python 中是没有 ++ 和 -- 的， python中的数字类型是不可变数据。也就是数字类型数据在 内存 中是不会发生改变，当变量值发生改变时，会新申请一块内存赋值为新值，然后将变量指向新的内存地址
            # i--
            # j++
            i -= 1
            j += 1
        return s[i + 1: j], j - i - 1 