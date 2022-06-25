class Solution:
    """
    88. 合并两个有序数组
    给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 思路：常见三种方法，方法1：将数组2放到数组1的后n位，快排 方法2：双指针，复制数组1，
        # 然双指针p1、p2从前往后分别遍历，将较小值从前往后依次放入数组1 方法3：三指针法，
        # p1,p2从后往前遍历比较，p初始指向nums1的末尾，将p1、p2指向的较大值依次放入
        # nums1的p--的位置
        # 这里直接使用最优解，三指针法
        # 1. 初始化
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # 2. while循环遍历并处理
        # 易错点 and
        # while p1 >= 0 and p2 >= 0:
        while p1 >= 0 or p2 >= 0:
            # 先处理两种特殊情况，就是有个数组先走完
            if p1 == -1:
                nums1[p] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[p] = nums1[p1]
                p1 -= 1
            elif nums1[p1] >= nums2[p2]:
               nums1[p] = nums1[p1]
            #    p -= 1
               p1 -= 1
            else:
               nums1[p] = nums2[p2] 
               p2 -= 1
            p -= 1