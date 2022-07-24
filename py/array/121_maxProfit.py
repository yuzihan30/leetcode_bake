class Solution:
    """
    121. 买卖股票的最佳时机
    给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
    """
    def maxProfit(self, prices: List[int]) -> int:
        # 思路：遍历每一项时，计算当前值和历史价格最低值之差, 并更新最大之差；同时更新历史最低值
        # 1. 初始化及特殊处理
        n = len(prices)
        ans, minPrice = 0, prices[0]
        # 2. 遍历
        for i in range(n):
            ans = max(ans, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        
        # 3. 返回结果值
        return ans
        