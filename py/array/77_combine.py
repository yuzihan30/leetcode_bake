class Solution:
    """
    77. 组合
    给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
    """
    # 将类内方法共享的变量抽离出来
    # __ans = [] # 结果列表
    # __cur = []   # 记录当前正在处理的一个组合
    # def __init__(self, ans=[], cur=[]):
    #     self.__ans = ans
    #     self.__cur = cur
    # 上面定义私有变量有问题，leetcode实例化一次，测试多次时，会将结果积累到ans中
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 思路：回溯法, 选好一个值，再选下一个值时，让start值加1， 让k值减1
        # 1. 初始化
        ans = []
        cur = []
        self.back_track(ans, cur, 1, n, k)
        return ans
    
    def back_track(self, ans: List[List[int]], cur: List[int], start: int, n: int, k: int) -> None:
        # 递归终止条件
        if k == 0:
            ans.append(cur.copy())
            # cur = [] # 易错点：不用清空，回溯的过程会不断压入弹出
            return
        
        # 回溯
        # for i in range(start, n): # 易错点
        for i in range(start, n+1):
            cur.append(i)
            # self.back_track(start+1, n, k-1) # 易错点
            self.back_track(ans, cur, i+1, n, k-1)
            cur.pop()
