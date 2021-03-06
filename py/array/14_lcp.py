class Solution:
    """
    14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 思路：解法比较多，时间复杂度基本都为O(mn)级别，这里使用横向扫描，对应还有纵向扫描法。
        # 核心思想就是集合交集满足结合律
        # 1. 初始化
        if not strs: # 空数组特殊处理
            return ''
        prev, num = strs[0], len(strs) # strs[0]当做第一个公共子串
        count = 0 # 记录最长公共子串的长度

        # 2. 遍历strs
        for i in range(1, num):
            prev = self.lcp(prev, strs[i])
            if not prev: # 如果遇到空串，提前终止循环
                break
        return prev


    def lcp(self, l: str, r: str) -> str:
        n = min(len(l), len(r))
        index = 0
        for i in range(n):
            # if l[i] != r[i]: # 易错点：如果一个串是另一个串的一部分， 就不会继续往下走
            if l[i] == r[i]:
                index += 1
            # else: # 易错点：如果一个串是另一个串的一部分， 就走不到这里了
            #     return l[:index]
            else:
                break
        return l[:index]



if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))