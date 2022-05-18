<!--
 * @Author: yuzihan yuzihanyuzihan@163.com
 * @Date: 2022-05-18 09:02:43
 * @LastEditors: yuzihan yuzihanyuzihan@163.com
 * @LastEditTime: 2022-05-18 09:03:33
 * @FilePath: /leetcode_bake/py/array/47_permuteUnique.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
class Solution:
    """
    47. 全排列 II
    给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 思路：回溯+剪枝
        # 1. 初始化及特殊处理
        if not nums:
            return []
        count = len(nums)
        stepNum = 0
        # 排序是为剪枝做准备，画图看一下树形结构，同一层如果某个数出现过，就剪枝
        sortedNums = sorted(nums) 
        path = [] 
        res = []
        # 记录哪些数使用过，已经存在在path里了, 应用了空间换时间的思想
        usedList = [0 for _ in sortedNums] 

        # 2. 调用回溯方法
        self.dfs(sortedNums, count, path, usedList, stepNum, res)

        # 3. 返回结果值
        return res

    def dfs(self, sortedNums: List[int], count: int, path: List[int], usedList: List[int], stepNum: int, res: List[List[int]]) -> None:
        # 终止递归条件
        if count == stepNum:
            res.append(path.copy()) # 不要遗漏
            return
        # 遍历sortedNums
        for i in range(count):
            # 46题全排列只需要这一个判断条件
            if usedList[i] == 1:
                continue
            # 47题全排列需要增加这一个判断条件做剪枝
            # 同一层从第二个数开始，如果前面使用过相同的数，就剪枝跳过
            # if i > 0 and usedList[i] == usedList[i-1] and usedList[i-1] == 1:
            if i > 0 and sortedNums[i] == sortedNums[i-1] and usedList[i-1] == 1:
                continue
            path.append(sortedNums[i])
            usedList[i] = 1
            self.dfs(sortedNums, count, path, usedList, stepNum + 1, res)
            # 回溯后恢复现场
            # path.pop(sortedNums[i])
            path.pop()
            usedList[i] = 0  