class Solution:
    """
    22. 括号生成
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    """
    def generateParenthesis(self, n: int) -> List[str]:
        # 思路：可以暴力解法，这里我们直接上回溯法
        # 1. 初始化和特殊处理
        if n <= 0:
            return []
        res = []
        
        # 2. 回溯
        # A代表当前括号字符数组（将字符串转为数组处理，方便使用数组方法，处理完之后再转回去），
        # l 代表左括号的数量，r 代表右括号的数量
        def backTrack(A: List[str], l: int, r: int):
            # 递归三部曲之1终止条件
            if len(A) == 2 * n:
                res.append(''.join(A))
                return  # 易错点：这里一定注意返回
            # 添加左括号的硬性条件
            # elif l < n:  # 易错点：不能用else
            if l < n and l >= r:
                A.append('(')
                backTrack(A, l + 1, r)
                # 当前括号处理完回溯后要删掉当前括号
                A.pop()
            # 添加右括号的硬性条件
            # elif l > r:  # 易错点：不能用else, 因为后面两种情况可能存在交集的情况
            if l > r and r < n:
                A.append(')')
                backTrack(A, l, r + 1)
                # 当前括号处理完回溯后要删掉当前括号
                A.pop()

        
        backTrack([], 0, 0)
        return res



