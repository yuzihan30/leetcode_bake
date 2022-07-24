class Solution:
    """
    122. 买卖股票的最佳时机 II
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润 。   
    """
    def maxProfit(self, prices: List[int]) -> int:
        # 思路：抽象成价格折线图，求出每个连续上升空间的和，连续上升空间又可拆分为子区间；
        # 最终转化为遍历过程中，求每个子上升区间之和，max(prices[i]-prices[i-1], 0)
        # 1. 初始化及特殊处理
        n = len(prices)
        ans = 0

        # 2. 遍历处理
        for i in range(1, n):
            ans += max(prices[i]-prices[i-1], 0)
        
        # 3. 返回结果值
        return ans
