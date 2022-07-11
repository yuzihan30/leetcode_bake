class Solution:
    """
    57. 插入区间
    给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 思路：分三个区间，左侧不重叠区间，中间重叠区间，右侧不重叠区间
        # 1. 初始化及特殊处理
        if not intervals and newInterval:
            return [newInterval]
        n = len(intervals)
        i = 0
        res = []

        # 2. 三个区间遍历处理
        # 左侧无重叠区间处理
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i = i + 1
        # 中间重叠区间合并(如果存在中间重叠区域)，边界相等也算重叠
        if i < n:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            # 关键点: 如果newInterval的右边界大于等于intervals[i]的左边界，
            # 就不断遍历intervals[i]
            while i < n and newInterval[1] >= intervals[i][0]:
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i = i + 1
            # res.append(newInterval) # 易错点
        # 涵盖i < n 和 i = n的情况
        res.append(newInterval)
        # 右侧无重叠区间处理
        while i < n:
            res.append(intervals[i])
            i = i + 1
        
        # 3. 返回结果值
        return res
