'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
参考思路：
https://www.bilibili.com/video/BV1H5411c7oC
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. 计算两个数组的长度
        len1 = len(nums1)
        len2 = len(nums2)

        # 2. 始终保证第一个数组是短数组，以短数组位计算基准，可以将计算复杂度降低到
        # O(log(min(len1,  len2))). 达到这种目有两种途径，一种是递归，一种直接数组位置互换
        if len1 > len2: 
            return self.findMedianSortedArrays(nums2, nums1) 
        
        # 3. 初始化短数组的二分法的区间范围及中位数，[0, len1], 左闭右闭，对应数组下标
        # 想象一下，i始终指向边界像右边那个值，极端的情况，nums数组边界右侧没有值时i=len1
        i_min, i_max, median = 0, len1, 0
        # 4. while循环、二分法处理短数组 易错点：i_min <= i_max, 包含等于
        while i_min <= i_max:
            # 4.1 根据二分法的思路初始化i的值
            i = (i_min + i_max) // 2
            # 4.2 初始化j的值, 可以通过数学推导得到i、j的和为(len1 + len2 + 1) // 2
            j = (len1 + len2 + 1) // 2 - i
            # 4.3 确定nums中的计算区间是右移还是左移，先处理左移情况（即左下值大于右上值）
            # i != len1 and j != 0防止数组越界, 易错点：越界条件要先放前面
            # if nums2[j-1] > nums1[i] and i != len1 and j != 0: 
            if i != 0 and j != len2 and nums1[i-1] > nums2[j] : 
                # 区间的右边界左移 易错点：注意闭区间
                # i_min = i + 1
                i_max = i - 1 # 关键点：区间的移动方向
            # 4.4 处理区间右移情况，（即左上大于右下）易错点：是elif不是else if
            elif i != len1 and j != 0 and nums2[j-1] > nums1[i]:
                # i_max = i - 1
                i_min = i + 1 
            # 4.5 否则就满足了计算中位数的条件  
            else: 
                left_max, right_min = 0, 0
                # 4.5.1 假设 len1 + len2 为奇数，计算左边的最大值即为中位数
                # 处理特殊情况 i = 0，即上边数组出现左边界左边没有值得情况 易错点：判断条件 i==0
                if i == 0: left_max = nums2[j-1]
                # 处理特殊情况 j = 0 , 即下边数组左侧无值得情况
                elif j == 0: left_max = nums1[i-1]
                # 处理通常情况
                else: left_max = max(nums1[i - 1], nums2[j - 1])
                # 易错点：不是/，而是%
                if (len1 + len2) % 2 == 1: return left_max

                # 4.5.2 处理 len1 + len2 为偶数的情况
                # 计算右边的最小值
                # 处理特殊情况 i = len1
                if i == len1: right_min = nums2[j]
                # 处理特殊情况 j = len2
                elif j == len2: right_min = nums1[i]
                # 处理通常情况
                else: right_min = min(nums1[i], nums2[j])
                return (left_max + right_min) / 2

# if __name__ == '__main__':
#   solution = Solution()
#   return_value = solution.findMedianSortedArrays([1,2,3,4], [1,3,5,7,8,9])
#   print(return_value)
