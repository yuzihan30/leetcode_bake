class Solution:
    """
    39. 组合总和
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 思路：回溯法，提前将整数数组排序可以达到剪枝的效果
        # 1. 初始化及特殊处理
        res = []
        sorted_candidates = sorted(candidates)
        count = len(sorted_candidates)

        # 2. 定义回溯方法, start是为了排除掉重复组合
        def back_track(start: int, path: List[int]):
            sum = 0
            for num in path:
                sum += num
            # 2.1 递归终止条件
            if sum > target:
                return
            if sum == target:
                # res.append(path)
                # 易错点：注意添加的是path的拷贝，而非path，否则res中添加的path最终结果指向同一个path
                res.append(path.copy()) 
                return 
            for i in range(start, count):
                path.append(sorted_candidates[i])
                back_track(i, path) 
                path.pop()
        
        # 3. 调用回溯方法
        back_track(0, [])
        
        # 4. 返回结果值
        return res