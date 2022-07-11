class Solution:
    """
    56. 合并区间
    以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 思路：排序加双指针，排序后，遍历合并区间的同时，更新start、end指针。
        # 更新start、end的规则是：intervals[i][0] > end则[start, end] = intervals[i]；
        # intervals[i][0] 小于等于 end，此时start不变，end = max(end, intervals[i][1])
        # 1. 初始化及特殊处理
        intervals.sort(key=lambda x : x[0])
        [start, end] = intervals[0]
        n = len(intervals)
        res = []

        # 2. 遍历处理，并更新start、end
        for i in range(1, n):
            if intervals[i][0] > end:
                res.append([start, end])
                [start, end] = intervals[i]
            else:
                end = max(end, intervals[i][1])
        res.append([start, end])

        # 3. 返回结果值
        return res
        
