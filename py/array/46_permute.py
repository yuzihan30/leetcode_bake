class Solution:
    """
    46. 全排列
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 思路： 深度优先遍历，回溯法
        # 1. 初始化及特殊处理
        if not nums:
            return []
        count = len(nums)
        res = []
        # used = []
        # step = 1
        # 易错点1，记录步数，其实等价于实时记录path中元素的索引，
        # 便于记录跟踪计算递归的终止条件
        step = 0
        path = []

        # 2. 调用回溯方法
        # _dfs(nums, count, step, path, used, res)
        self._dfs(nums, count, step, path, res)

        # 3. 返回结果值
        return res

    def _dfs(self, nums: List[int], count: int, step: int, path: List[int], res: List[List[int]]):
        if step == count:
            # res.append(path)
            # 易错点2，注意深拷贝，不然随着回溯进行，path指向的列表会清空成空列表
            # path是一个公共空间，随着程序执行不断发生变化，回溯到最后path是空的
            # 如果不深拷贝，res中每个元素都指向同一个空列表path
            res.append(path[:])
            return
        for num in nums:
            if num in path:
                continue
            path.append(num)
            self._dfs(nums, count, step + 1, path, res)
            path.remove(num)