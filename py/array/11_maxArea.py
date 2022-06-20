class Solution:
    """
    11. 盛最多水的容器
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。
    """

    def maxArea(self, height: List[int]) -> int:
        # 思路: 直接上最优方法，双指针法，关键是每次移动短板，这样才会找到更大的值
        # 1. 初始化左右指针、最大面积
        num = len(height)
        # max_area = min(height[0], height[num - 1]) * (num - 1)
        max_area = 0
        l, r = 0, num - 1

        # 2. 移动指针
        # while 0 <= l <= r and l <= r <= num - 1:
        while l <= r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                # 易错点：python 中数字类型的值是不可变的, 所以没有自增、自减运算符
                l = l + 1
            else:
                r = r - 1

        return max_area


# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))